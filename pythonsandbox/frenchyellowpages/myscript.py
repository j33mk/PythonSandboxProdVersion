import time
import json
import os
import requests
from bs4 import BeautifulSoup
import concurrent.futures
import pandas as pd
import glob




listFiles=glob.glob("Hauts-de-France/*.html")
list = []
try:
    for file in listFiles:
        with open(file, encoding="utf-8") as f:
            data = f.read()
            soup = BeautifulSoup(data, 'html.parser')
            resultIntros = soup.find_all("li",class_="bi-bloc")
            for li in resultIntros:
                try:
                    url = "https://www.pagesjaunes.fr/pros/detail?bloc_id={0}&no_sequence=1&code_rubrique=58056600".format(li.get("id").replace("bi-bloc-",""))
                    list.append({"Link":url})
                except Exception as ex:
                    print(ex)
                finally:
                    pass               
except Exception as ex:
        print(ex)
finally:
    frame = pd.DataFrame(list,columns=["Link"])
    frame.to_excel("{0}.xlsx".format("Hauts-de-France"))
    
   



    