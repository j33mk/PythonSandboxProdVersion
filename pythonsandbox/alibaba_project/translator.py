import googletrans
from googletrans import Translator
import pandas as pd
import concurrent.futures
import os


def translate_hebrew(my_col,df):
    translator = Translator()
    result_output = {}
    for item in df[my_col]:
        result_output[item] = translator.translate(item,src='en',dest='he').text
    return result_output

def translate_file(file_name):
    df = pd.read_json('scrap_done/{0}'.format(file_name))
    input_colons =['name','details','category']
    try:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(translate_hebrew,col,df) for col in input_colons]
            for f in futures:
                df.replace(f.result(),inplace=True)

    except Exception as ex:
        print(ex)
    finally:
        print('File name is {0}'.format(file_name))
        df.to_csv('scrap_done/csvs/'+file_name.replace('json','csv'),index=False)
        print('file saved as csv')
        print("---------------------------------------------------------------------------------\n")




files = os.listdir('scrap_done/')
for f in files:
    translate_file(f)

