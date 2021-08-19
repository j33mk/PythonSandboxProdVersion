from requests import Session
from lxml import html
import re
import csv
import os

session = Session()
session.head('https://www.google.com/')

def google_search(input_string):
    response = session.get(
        url = 'https://www.google.com/search',
        params = {
          "q": input_string
        }
    )
    return response

def get_email(response):
  tree = html.fromstring(response.content)
  search_results = tree.xpath("//div[@class='BNeawe s3v9rd AP7Wnd']")
  for index, search_result in enumerate(search_results):
    headings = search_result.xpath("./text()")
    for idx, heading in enumerate(headings):
      if "\nEmail: " == heading:
        r = re.compile(".*@.*")
        text = tree.xpath("//div[@class='BNeawe s3v9rd AP7Wnd']['+index+']/span['+idx+']/text()")
        return list(filter(r.match, text))[0]
  return None 

def save_email(email):
  with open("output.csv", 'a+') as f:
    csv_columns = ["Company name", "Email"]
    writer = csv.writer(f)
    if os.stat("output.csv").st_size == 0:
      writer.writerow(csv_columns)
    writer.writerow([company_name, email])

company_name = "All Things Travel Lara"
input_string = company_name.replace(' ', '+')

response = google_search(input_string)
if response.status_code == 200:
  email = get_email(response)
  save_email(email)