from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import json
import os
import requests
from bs4 import BeautifulSoup

def get_product_details(product_link):
    video = ""
    details = ""
    origin = ""
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        response = requests.get('{0}'.format(product_link),headers=headers).text
        soup = BeautifulSoup(response,'html.parser')
        try:
            video = soup.find("video").get("src")
        except:
            video = "video"
        try:
            details = soup.find("div",class_="do-overview").text.replace(" ","").replace("\n"," ")
        except:
            details = "details"
        try:
            origin = soup.find("div",class_="company-name-container").text.replace(" ","").replace("\n","")
        except:
            origin = "origin"
    except Exception as ex:
        print(ex)
    finally:
        return {"video":video,"details":details,"origin":origin}
 
    
def get_items(search,page):
    search = search.replace(" ","_")
    url = "https://www.alibaba.com/products/{}.html?IndexArea=product_en&page={}".format(   
        search, page
    )
    print(url)
    output = []
    driver.get(url)    
    time.sleep(1)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    items = driver.find_elements_by_css_selector(".J-offer-wrapper")
    try:
        for i in items:
            try:
                product_url = i.find_element_by_css_selector("h4 a").get_attribute("href")
                product_details = get_product_details(product_url)
                video = product_details.get('video')
                details= product_details.get('details')
                origin = product_details.get('origin')
            except:
                product_url = "null"
            try:
                product_name = i.find_element_by_css_selector("h4").text
            except:
                product_name = ""
            try:
                price = i.find_element_by_css_selector(".elements-offer-price-normal").text
            except:
                price = "$0"
            try:
                img_div = i.find_element_by_css_selector(".seb-img-switcher__imgs")
                img_url = img_div.get_attribute("data-image")
                img_url = "https:"+img_url
                img_url = img_url.replace("_300x300.jpg","")
            except:
                img_url = ""
            output_item = {"name": product_name, "price": price, "url": product_url,"video":video,"details":details,"origin":origin, "image": img_url,"category":"Home > All Industries > Machinery > "+search}
            output.append(output_item)
    except Exception as ex:
        print(ex)
    finally:
        return output


categories_list = [
    'Agricultural Machinery & Equipment',
    'Apparel & Textile Machinery',
    'Building Material Machinery',
    'Chemical & Pharmaceutical Machinery',
    'Cleaning Equipment',
    'Electric Equipment Making Machinery',
    'Energy & Mineral Equipment',
    'Engineering & Construction Machinery',
    'Environmental Machinery',
    'Food & Beverage Machinery',
    'Home Product Making Machinery',
    'Industrial Robots',
    'Industry Laser Equipment',
    'Machine Tool Equipment',
    'Machinery Accessories',
    'Machinery Service',
    'Material Handling Equipment',
    'Metal & Metallurgy Machinery',
    'Other Machinery & Industry Equipment',
    'Paper Production Machinery',
    'Plastic & Rubber Processing Machinery',
    'Printing Machine',
    'Refrigeration & Heat Exchange Equipment',
    'Tobacco & Cigarette Machinery',
    'Welding Equipment',
    'Woodworking Machinery'    
]
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)



for category in categories_list:
    try:
        print("Scraping Category: {0}".format(category))
        page = 1
        all_items = []
        while True:
            print("Getting Page {0}".format(page))
            results = get_items(category,page)
            all_items+=results
            if len(results)==0:
                break
            page +=1
    except Exception as ex:
        print(ex)
    finally:
        json.dump(all_items,open("{0}.json".format(category),"w"),indent=2)



driver.close()

# try:
#     all_items = []
#     for category in categories_list:
#         print("Scrpaing "+category)
#         page = 1
#         search = category
#         while True:
#             print("getting page", page)
#             results = get_items(search, page)
#             all_items += results

#             if len(results) == 0:
#                 break

#             page += 1

#     json.dump(all_items,open("products.json","w"),indent=2)
#     driver.close()

# except Exception as ex:
#     print(ex)
# finally:
#     json.dump(all_items,open("products.json","w"),indent=2)
#     driver.close()

