import time
import json
import os
import requests
from bs4 import BeautifulSoup
import concurrent.futures
import pandas as pd


list = []
name=""
address=""
linkHref=""
try:
    with open("index.html", encoding="utf-8") as f:
        data = f.read()
        soup = BeautifulSoup(data, 'html.parser')

        resultIntros = soup.find_all("article",class_="result-intro")
        for intro in resultIntros:
            if intro is not None:
                try:
                    name = intro.find("h4",class_="result-intro__heading").text
                    print("Scraping: "+name)
                    address =intro.find("p",class_="result-intro__address").text
                    linkHref = intro.find("a")["href"]
                    list.append({"Name":name,"Address":address,"Website":linkHref,"Email":"","Telephone":""})
                except Exception as ex:
                    pass
                finally:
                    pass
                
except Exception as ex:
    print(ex)
finally:
    pass
    frame = pd.DataFrame(list,columns=["Name","Address","Website","Email","Telephone"])
    frame.to_excel("australia-capital-territory.xlsx")


    