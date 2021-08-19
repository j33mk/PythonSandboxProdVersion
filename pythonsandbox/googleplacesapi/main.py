import pandas as pd
import requests
import json

api_key = "AIzaSyAT5cEEz1btzI5nrEiI1P08vmyY7PBmQrs"
excel_file = 'mybook.xlsx'
places = pd.read_excel(excel_file)
final_output = []
places_list = places.values.tolist()
i = 0

try:
    for place in places_list:
        print(str(i)+" | "+place[0])
        i = i+1
        address_search = place[0]

        url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=" + address_search + \
            "&inputtype=textquery&fields=name,formatted_address,permanently_closed&key=" + api_key
        response = requests.get(url).json()
        cand = response['candidates']
        if(cand==[]):
            final_output.append(
                    {"name": address_search, "permenantely_closed": 'Not Yet'})
        for c in cand:
            k = c.get('permanently_closed')
            if(k is None):
                final_output.append(
                    {"name": address_search, "permenantely_closed": 'Not Yet'})
            if(k == True):
                final_output.append(
                    {"name": address_search, "permenantely_closed": 'Yes'})
            else:
                final_output.append(
                    {"name": address_search, "permenantely_closed": 'Not Yet'})
except Exception as ex:
    print(ex)
finally:
    json.dump(final_output, open(
        "{0}.json".format("finaloutput"), "w"), indent=2)
