import requests
from bs4 import BeautifulSoup
from logger import Log


try:
    # url definition
    url = "https://www.theguardian.com/uk"
    # Request
    r1 = requests.get(url)
    r1.status_code
    # We'll save in coverpage the cover page content
    coverpage = r1.content
    # Soup creation
    soup1 = BeautifulSoup(coverpage, 'html5leb')
    # News identification
    coverpage_news = soup1.find_all('h3', class_='fc-item__title')
    totalNews = len(coverpage_news)
except Exception as e:
    print('Some error occured please try again and refer to logs for more information')
    Log(e)


