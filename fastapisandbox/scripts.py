import requests
from bs4 import BeautifulSoup
from logger import Log
import json


try:
    # url definition
    # url = "https://www.theguardian.com/uk"
    url = "https://www.dawn.com/"
    # Request
    r1 = requests.get(url)
    r1.status_code
    # We'll save in coverpage the cover page content
    coverpage = r1.content
    # Soup creation
    soup1 = BeautifulSoup(coverpage, 'html5lib')
    # News identification
    # coverpage_news = soup1.find_all('h3', class_='fc-item__title')
    coverpage_news = soup1.find_all('article')
    my_links = []
    for i in coverpage_news:
        link = i.find('a',href=True)
        if link is None:
            continue
        my_links.append(link['href'])
        print(link['href'])

    totalNews = len(coverpage_news)
    result = {
        "TotalNews":totalNews,
        "news_links":my_links
    }
    output = json.dumps(result)
    print(output)
    with open('output.json', 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=4)
        print('File is saved')
except Exception as e:
    print('Some error occured please try again and refer to logs for more information')
    Log(e,str(os.path.basename(__file__)))


