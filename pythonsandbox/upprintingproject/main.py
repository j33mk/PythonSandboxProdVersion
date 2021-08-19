import pandas as pd
import requests
import json
from bs4 import BeautifulSoup


products = pd.read_excel('productslist.xlsx')
jsonOutput = []
response = requests.get(products["Link"][0]).text
soup = BeautifulSoup(response,'html.parser')


for i in range(0,len(products)):

    response = requests.get(products["Link"][i]).text
    soup = BeautifulSoup(response, 'html.parser')
    shortdesc=str(soup.find("div", class_="sms-wgt-text-image scroll-lazy wgt-txt-list_styles-check_list_primary wgt-txt-list_display_styles-list_group_inline"))
    longdesc=str(soup.find("div", class_="overview-tab-wrapper content-tab-wrapper"))
    specsmaterial=str(soup.find("div", class_="paper-and-specs-tab-wrapper content-tab-wrapper"))
    result = {
        "Product Name":products["Product"][i],
        "Product Link":products["Link"][i],
        "Variation 1 Name":"",
        "Attribute 1 value(s)":"",
        "Variation 2 Name":"",
        "Attribute 2 value(s)":"",
        "Variation 3 Name":"",
        "Attribute 3 value(s)":"",
        "Variation 4 Name":"",
        "Attribute 4 value(s)":"",
        "Variation 5 Name":"",
        "Attribute 5 value(s)":"",
        "Variation 6 Name":"",
        "Attribute 6 value(s)":"",
        "Variation 7 Name":"",
        "Attribute 7 value(s)":"",
        "Variation 8 Name":"",
        "Attribute 8 value(s)":"",
        "Variation 9 Name":"",
        "Attribute 9 value(s)":"",
        "Variation 10 Name":"",
        "Attribute 10 value(s)":"",
        "Price":"",
        "Short Description":shortdesc,
        "Long Description":longdesc,
        "Specs/Material":specsmaterial
    }
    jsonOutput.append(result)

outputframe = pd.DataFrame(jsonOutput)
outputframe.to_excel("finalOutput.xlsx")