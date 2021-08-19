from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import json
import os
import requests
from bs4 import BeautifulSoup
import concurrent.futures



def get_product_details(product_link):
    print('.', end='')
    video = ""
    details = ""
    origin = ""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        response = requests.get('{0}'.format(product_link), headers=headers).text
        soup = BeautifulSoup(response, 'html.parser')
        try:
            video = soup.find("video").get("src")
        except:
            video = "video"
        try:
            details = soup.find("div", class_="do-overview").text.replace(" ", "").replace("\n", " ")
        except:
            details = "details"
        try:
            origin = soup.find("div", class_="company-name-container").text.replace(" ", "").replace("\n", "")
        except:
            origin = "origin"
    except Exception as ex:
        print(ex)
    finally:
        return {"video": video, "details": details, "origin": origin}


def get_items(search, page):
    search = search.replace(" ", "_")
    url = "https://www.alibaba.com/products/{}.html?IndexArea=product_enandpage={}".format(
        search, page
    )
    print(url)
    output = []
    driver.get(url)

    # time.sleep(1)
    # driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    # time.sleep(1)
    # driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    # time.sleep(1)

    time.sleep(2)  # Allow 2 seconds for the web page to open
    scroll_pause_time = 1  # You can set your own pause time. My laptop is a bit slow so I use 1 sec
    screen_height = driver.execute_script("return window.screen.height;")  # get the screen height of the web
    i = 1

    while True:
        # scroll one screen height each time
        driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
        i += 1
        time.sleep(scroll_pause_time)
        # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
        scroll_height = driver.execute_script("return document.body.scrollHeight;")
        # Break the loop when the height we need to scroll to is larger than the total scroll height
        if (screen_height) * i > scroll_height:
            break

    items = driver.find_elements_by_css_selector(".J-offer-wrapper")
    try:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(scrap, i, search) for i in items]

            for f in futures:
                output.append(f.result())

        return output

    except Exception as ex:
        print('this fucker called')
        print(ex)

def scrap(i, search):
    try:
        product_url = i.find_element_by_css_selector("h4 a").get_attribute("href")
        product_details = get_product_details(product_url)
    except:
        product_url = "null"
    try:
        origin = product_details.get('origin')
    except:
        origin = "null"
    try:
        details = product_details.get('details')
    except:
        details = "null"
    try:
        video = product_details.get('video')
    except:
        video = "null"
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
        img_url = "https:" + img_url
        img_url = img_url.replace("_300x300.jpg", "")
    except:
        img_url = ""

    output_item = {"name": product_name, "price": price, "url": product_url, "video": video, "details": details,
                   "origin": origin, "image": img_url,
                   "category": "Home > All Industries > Machinery > " + search}

    return output_item

categories_list = [
    'Paper Production Machinery',
    'Plastic and Rubber Processing Machinery',
    'Printing Machine',
    'Refrigeration and Heat Exchange Equipment',
    'Tobacco and Cigarette Machinery',
    'Welding Equipment',
    'Woodworking Machinery'
]
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

for category in categories_list:
    try:
        print("\nScraping Category: {0}".format(category))
        page = 1
        all_items = []
        while True:
            print("\nGetting Page {0}".format(page))
            results = get_items(category, page)
            all_items += results
            if len(results) == 0:
                break
            page += 1

        json.dump(all_items, open("{0}.json".format(category), "w"), indent=2)
    except Exception as ex:
        print(ex)

driver.close()
