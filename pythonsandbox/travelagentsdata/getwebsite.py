import requests
import pandas as pd
import json
from bs4 import BeautifulSoup


data = pd.read_excel("southaust.xlsx",sheet_name="Sheet1")
newdata = pd.DataFrame(columns=data.columns)
url = "https://autocomplete.clearbit.com/v1/companies/suggest?query="
list = []
for index, row in data.iterrows():
    try:
        data = requests.get(url+row["Name"]).json()[0]['domain']
        websitehtml = requests.get(data)
        soup = BeautifulSoup(websitehtml.text, 'html.parser')
        phone = get_phone(soup)
        email = get_email(soup)
        print({"Name":row["Name"],"Address":row["Address"],"Website":data,"Email":email,"Phone":phone})
    except Exception as ex:
        print({"Name":row["Name"],"Address":row["Address"],"Website":data,"Email":"","Phone":""})
    finally:
        pass


def get_phone(soup):
    try:
        phone = soup.select("a[href*=callto]")[0].text
        return phone
    except:
        pass

    try:
        phone = re.findall(r'\(?\b[2-9][0-9]{2}\)?[-][2-9][0-9]{2}[-][0-9]{4}\b', response.text)[0]
        return phone
    except:
        pass

    try:
       phone = re.findall(r'\(?\b[2-9][0-9]{2}\)?[-. ]?[2-9][0-9]{2}[-. ]?[0-9]{4}\b', response.text)[-1]
       return phone
    except:
        print ('Phone number not found')
        phone = ''
        return phone



def get_email(soup):
    try:
        email = re.findall(r'([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)', response.text)[-1]
        return email
    except:
        pass

    try:
        email = soup.select("a[href*=mailto]")[-1].text
    except:
        print ('Email not found')
        email = ''
        return email


