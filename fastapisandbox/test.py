from logger import Log
import os
try:
    print(1/0)
except Exception as e:
    Log(e,str(os.path.basename(__file__)))