import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import datetime

exception_list=[]
def get_tickers(html_response):
    try:
        contract_rows = html_response.findAll('tr',class_='contractRow')
        tickers = []
        for contract in contract_rows:
            last_td = (contract.findAll('td')[-1]).text
            tickers.append(last_td)
        return tickers
    except Exception as ex:
        exception_list.append(ex)
        return []
    
def get_class_names(html_response):
    try:
        contract_rows = html_response.findAll('tr',class_='contractRow')
        class_names = []
        for contract in contract_rows:
            last_td = (contract.findAll('td')[-2]).text
            class_names.append(last_td)
        return class_names
    except Exception as ex:
        exception_list.append(ex)
        return []

def get_class_contract(html_response):
    try:
        contract_rows = html_response.findAll('td',class_='classContract')
        class_contract = []
        for contract in contract_rows:
            a = contract.find('a').text
            class_contract.append(a)
        return class_contract
    except Exception as ex:
        exception_list.append(ex)
        return []

def get_filing_date(html_response):
    try:
        filing_date = html_response.find('div',class_='info').text
        return filing_date
    except Exception as ex:
        exception_list.append(ex)
        return ""

def get_period_report(html_response):
    try:
        period_date = html_response.findAll('div',class_='info')[-1].text
        return period_date
    except Exception as ex:
        exception_list.append(ex)
        return ""

def read_xml(xml_link,html_link):
    print("Scraping Process Started...Please don't close this and let the process finish")
    print(f"Scraping...{xml_link}")
    final_output = {}
    try:
        xml_response = BeautifulSoup(requests.get(xml_link).text,'xml')
        final_output["url"] = xml_link
        final_output["html_link"] = html_link
        final_output["cik"] = xml_response.find('cik').text
        final_output["seriesName"] = xml_response.find('seriesName').text
        final_output["seriesId"] = xml_response.find('seriesId').text
        final_output["classId"]=get_formatted_classids(xml_response.findAll('classId'))
        final_output["TickerSymbols"] = ",".join(get_tickers((html_link)))
        final_output["regName"] = xml_response.find("regName").text
        final_output["regCik"] = xml_response.find("regCik").text
        final_output["regLei"] = xml_response.find("regLei").text
        final_output["regStreet1"] = xml_response.find("regStreet1").text
        final_output["regCity"] = xml_response.find("regCity").text
        final_output["regStateConditional"] = xml_response.find('regStateConditional')['regCountry']+','+xml_response.find('regStateConditional')['regState']
        final_output["regZipOrPostalCode"] = xml_response.find("regZipOrPostalCode").text
        final_output["regPhone"] = xml_response.find("regPhone").text
        final_output["seriesName"] = xml_response.find("seriesName").text
        final_output["seriesId"] = xml_response.find("seriesId").text
        final_output["seriesLei"] = xml_response.find("seriesLei").text
        final_output["repPdEnd"] = xml_response.find("repPdEnd").text
        final_output["repPdDate"] = xml_response.find("repPdDate").text
        final_output["totAssets"] = xml_response.find("totAssets").text
        final_output["totLiabs"] = xml_response.find("totLiabs").text
        final_output["netAssets"] = xml_response.find("netAssets").text
        get_invs_df2 = get_invs_or_secs(xml_response)
        return pd.DataFrame([final_output]).join(get_invs_df2,how="right").fillna(method='ffill')
    except Exception as ex:
        exception_list.append(ex)
        return []
    
def get_invs_or_secs(xml_response):
    try:
        invstOrSec = xml_response.findAll('invstOrSec')
        output = []
        #my machine can't handle large datasets.. remove the [0:20] part for future references
        for i in invstOrSec:
            try:
                i_list=[]
                i_list.append(i.find('name').text)
                i_list.append(i.find('lei').text)
                i_list.append(i.find('cusip').text)
                i_list.append(i.find('identifiers').find('isin')['value'])   
                i_list.append(i.find('balance').text)
                i_list.append(i.find('units').text)
                i_list.append(i.find('curCd').text)
                i_list.append(i.find('valUSD').text)
                i_list.append(i.find('pctVal').text)
                i_list.append(i.find('payoffProfile').text)
                i_list.append(i.find('assetCat').text)
                i_list.append(i.find('issuerCat').text)
                i_list.append(i.find('invCountry').text)
                i_list.append(i.find('isRestrictedSec').text)
                i_list.append(i.find('fairValLevel').text)
                output.append(tuple(i_list))
            except Exception as ex:
                exception_list.append(ex)

        return pd.DataFrame(output,columns=["<invstOrSec><name>","<lei>","<cusip>",'<identifiers><isin value="XXXXXXX"/>',"<balance>","<units>","<curCd>","<valUSD>","<pctVal>","<payoffProfile>","<assetCat>","<issuerCat>","<invCountry>","<isRestrictedSec>","<fairValLevel>"])
    except Exception as ex:
        exception_list.append(ex)

def get_formatted_classids(classIds):
    ids = []
    for c in classIds:
        ids.append(c.text)
    return ",".join(ids)

def get_html_response(html_link):
    try:
        return BeautifulSoup(requests.get(html_link).text,'html.parser')
    except Exception as ex:
        exception_list.append(ex)
        return ""

def get_xml_response(xml_link):
    try:
        return BeautifulSoup(requests.get(xml_link).text,'xml')
    except Exception as ex:
        exception_list.append(ex)
        return ""

xml_link = "https://www.sec.gov/Archives/edgar/data/36405/000175272420251139/primary_doc.xml"
html_link = "https://www.sec.gov/Archives/edgar/data/911507/000175272420007705/0001752724-20-007705-index.htm"

def create_csv(xml_link,html_link):
    try:
        #handle logic here like get xml and html response at first and then do processing :)
        #this will save amount of request sent to server
        #then read the url list and get all necessary links from there
        #build the corresponding csv as mentioned
        #then run these two functions one by one
        #fix naming convention for the functions
        df1 = read_xml(xml_link,html_link)
        file_name = df1.iloc[1]['seriesId']
        df1.to_csv(f"{file_name}.csv",mode="w",index=False)
        print(f"{file_name}.csv created")
    except Exception as ex:
        exception_list.append(ex)

def create_xlsx(xml_link,html_link):
    try:
        df1 = read_xml(xml_link,html_link)
        file_name = df1.iloc[1]['seriesId']
        df1.to_excel(f"{file_name}.xlsx",index=False)
        print(f"{file_name}.xlsx created")
    except Exception as ex:
        exception_list.append(ex)

def create_log(exception_list):
    try:    
        with open('mylog.log','a') as f:
            f.write("\n")
            f.write(f'Log has been created on {datetime.datetime.now()}')
            f.write("\n")
            f.write("------------------------------------------------------------------------------")
            f.write("\n")
            numbering = 1
            for ex in exception_list:
                f.write(f"{numbering}. {ex}")
                f.write("\n")
                numbering=numbering+1
            f.write("------------------------------------------------------------------------------")
            print('log has been created')
    except Exception as ex:
        pass

def build_html_file(html_response,row,html_link,colHVal,colGVal,colEVal):
    final_output = {}
    final_output['series url for this landing page'] = html_link
    final_output['Filer CIK'] = row['regName']
    final_output['CIK'] = row['cik']
    final_output['Series'] = row['seriesId']
    final_output['Series Name'] = row['seriesName']
    final_output['Filing Date'] = get_filing_date(html_response)
    final_output['Period Of Report'] = get_period_report(html_response)
    final_output['Url for html version of NPORT-P'] = colHVal
    final_output['Url for xml version of NPORT-P'] = colGVal
    final_output['Url for .txt version of NPORT-P'] = colEVal
    final_output['Url for nport-ex htm version'] = 'https://www.sec.gov/Archives/edgar/data/36405/000175272420251139/vg500index093020.htm'
    df1 = pd.DataFrame([final_output])
    classes = pd.DataFrame(get_class_contract(html_response),columns=["Class/Contract"])
    class_names = pd.DataFrame(get_class_names(html_response),columns=["Class Name"])
    ticker_symbols = pd.DataFrame(get_tickers(html_response),columns=["Ticker Symbol"])
    df1 = df1.join(classes,how="right").join(class_names,how="").join(ticker_symbols,how="").fillna(method='ffill')




create_log(exception_list)
    
#create_csv(xml_link,html_link)
def build_files():
    try:
        target_file = pd.read_excel("target.xlsx",sheet_name="NP_2019Q3-2010Q3",usecols = "E,F,G,H",index_col=None)
        for row in target_file.iterrows():
            print(row[1][4])
        #file_name E
        #Landing_page F
        #XML_Version G
        #HTML_Version H
        # htm = "https://www.sec.gov/Archives/edgar/data/36405/000175272420251139/0001752724-20-251139-index.htm"
        # htm_resp = get_html_response(htm)
        # print(get_filing_date(htm_resp))
        # print(get_period_report(htm_resp))
        # print(get_tickers(htm_resp))
        # print(get_class_contract(htm_resp))
        # print(get_class_names(htm_resp))
    except Exception as ex:
        print(ex)
        # print('Either you are not connected to internet or some another error occured. Please refer to logs')
        # exception_list.append(ex)


build_files()
create_log(exception_list)