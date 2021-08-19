from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time
import json
import os
import requests
from bs4 import BeautifulSoup
import itertools

chrome_options = Options()
driver = webdriver.Chrome()

xl_file = pd.read_excel("test_sheet.xlsx", sheet_name="Sheet1")
finalOutputData = pd.DataFrame(columns=xl_file.columns)
xlsxData = []

for index, row in xl_file.iterrows():
    print(row['Product Name'])
    try:
        productName = row['Product Name']
        url = row['Product Link']
        driver.get(url)   
        time.sleep(5)
        attributes_section = driver.find_element_by_xpath('//*[@id="calculator"]/div[1]/div') #locate div with id=calculator, get first div child, div[id=calculator]/div/div --- sometimes crashes because the page is not loaded, can be fixed
        all_attributes = attributes_section.find_elements_by_xpath('./div') #all children divs
        ddlsDicts = []
        for attr in all_attributes:
            try:
                attribute_label = attr.find_element_by_xpath(".//label[contains(@class, 'calculator-label')]").text
                # print(attribute_label)
                allDropDowns = attr.find_elements_by_xpath(".//custom-dropdown[@class='ng-isolate-scope']")
                for dropDown in allDropDowns:
                    ddl = []
                    ul = dropDown.find_element_by_xpath(".//ul[@class='dropdown-menu']")
                    vals = ul.find_elements_by_xpath('.//span[contains(@class,"dropdown-link-text")]')
                    for val in vals:
                        f = val.get_attribute("innerHTML")
                        soup = BeautifulSoup(f,'html.parser').getText()
                        # print({attribute_label:soup})
                        ddl.append({attribute_label:soup})
                        # valsList.append(soup)
                        #valsList.append(soup)
                    # print(valsList)
                    ddlsDicts.append(ddl)
                    # print("-----\n")
            except:
                pass
        possibleCombos = list(itertools.product(*ddlsDicts))
        for k in possibleCombos:
            recordEntry = {
                "Product Name":row("Product Name"),
                "Product Link":row("Product Link"),
                "Price":"$16.48",
                "Short Description":row("Short Description"),
                "Long Description":row("Long Description"),
                "Specs/Material":row("Specs/Material")
            }
            generateColAttrLabels = []
            generateColValLabels = []
            count=0
            for i in range(1,len(k)+1):
                generateColAttrLabels.append("Variation {0} Name".format(i))
                generateColValLabels.append("Attribute {0} value(s)".format(i))
            for f in k:
                for i in f:
                    recordEntry.update({generateColAttrLabels[count]:i.replace(":","")})
                    recordEntry.update({generateColValLabels[count]:f[i]})
                count=count+1
            xlsxData.append(recordEntry)
        df = pd.DataFrame(xlsxData)
        df.to_excel("/generatedFiles/{0}.xlsx".format(row("Product Name")))
    except Exception as ex:
        print(ex)
    finally:
        driver.close()





