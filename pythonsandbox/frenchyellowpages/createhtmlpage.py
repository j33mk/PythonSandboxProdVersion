import glob
from dominate import document
import pandas as pd
from dominate.tags import *


df = pd.read_excel('Hauts-de-France.xlsx') # can also index sheet by name or fetch all sheets
links = df['Link'].tolist()


with document(title='Hauts-de-France') as doc:
    h1('Links')
    for link in links:
        li(a(link,href=link))
with open('Hauts-de-France.html', 'w') as f:
    f.write(doc.render())