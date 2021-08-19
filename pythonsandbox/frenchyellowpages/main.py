import requests
from bs4 import BeautifulSoup


regions = [
    {"region":'Auvergne-Rhône-Alpes',"pages":99},
    {"region":'Bourgogne-Franche-Comté',"pages":32},
    {"region":'Bretagne',"pages":0},
    {"region":'Centre-Val de Loire',"pages":0},
    {"region":'Centre-Val de Loire',"pages":0},
    {"region":'Grand Est',"pages":0},
    {"region":'Hauts-de-France',"pages":0},
    {"region":'Ile-de-France',"pages":0},
    {"region":'Normandie',"pages":0},
    {"region":'Nouvelle-Aquitaine',"pages":0},
    {"region":'Occitanie',"pages":0},
    {"region":'Pays de la Loire',"pages":0},
    {"region":'Provence-Alpes-Côte d’Azur',"pages":0},
]
regionName = regions[0]["region"]
pages = regions[0]["pages"]
pageNo = 1
headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36'}
url="https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=ophtalmologue&ou=Grand-Est&idOu=R44&proximite=0&quoiQuiInterprete=ophtalmologue&contexte=j2OLk7V6t1edWFnJvJpv1w%3D%3D&page=2"

html = requests.get(url,headers=headers).text
soup = BeautifulSoup(html,'html.parser')
print(soup)