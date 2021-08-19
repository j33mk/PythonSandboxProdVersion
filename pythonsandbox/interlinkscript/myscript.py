import requests
import csv
import pandas as pd
from bs4 import BeautifulSoup


target_products = pd.read_excel('interlink-bad-price.xlsx').values.tolist()
fixed_products = []
products_fixed = 1
# for product in target_products:
#     print(product[0]+' || '+str(product[2])+' || '+str(product[3]))
# # print(target_products[0][0]) #Product Name
# # print(target_products[0][2]) #SKU
# # print(target_products[0][3]) #Catalog
try:
    for t_product in target_products:
        print('Processing: '+str(products_fixed))
        products_fixed = products_fixed+1
        query = {'q':t_product[0]}
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        response = requests.get('https://interlinksupply.com/catalogsearch/result/',params=query,headers=headers).text
        soup = BeautifulSoup(response,'html.parser')
        getAllProducts = soup.find("ol", {"class":"products list items product-items same-height"}).findAll('li')
        for product in getAllProducts:
            p = product.find("a",{"class":"product-item-link"}).text.strip()
            q = query.get('q')
            if len(q.strip()) == len(p.strip()) and q.strip() == p.strip():
                price1 = product.find("span",{"class":"price-wrapper"})
                if price1:
                    out = {'product':p,'price':price1.text.strip(),'message':'','SKU':t_product[2],'Catalog':t_product[3]}
                    print(out)
                    fixed_products.append(out)
                price2 = product.find("span",{"class":"price"})
                if price2:
                    out = {'product':p,'price':price2.text.strip(),'message':'','SKU':t_product[2],'Catalog':t_product[3]}
                    print(out)
                    fixed_products.append(out)
                message = product.find("span",{"class":"amasty-hide-price-text"})
                if message:
                    out = {'product':p,'price':'$0','message':message.text.strip(),'SKU':t_product[2],'Catalog':t_product[3]}
                    print(out)
                    fixed_products.append(out)
                    
        print('\n')
    final = pd.DataFrame(fixed_products)
    final.to_excel('fixed_prices2_final.xlsx')
except Exception as error:
    print(error)    
finally:
    final = pd.DataFrame(fixed_products)
    final.to_excel('fixed_prices2_final.xlsx')


