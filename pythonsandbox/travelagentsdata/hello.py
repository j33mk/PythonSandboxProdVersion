import requests
import os
from utilfunctions import download_user_contents


response = requests.get('https://randomuser.me/api')
data = response.json()
download_user_contents(data)



