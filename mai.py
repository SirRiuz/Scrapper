
from hyperHandler import Hyper
import sys
from requestmap import *



banner = '''
   _____                                      
  / ____|                                     { v1 }
 | (___   ___ _ __ __ _ _ __  _ __   ___ _ __ 
  \___ \ / __| '__/ _` | '_ \| '_ \ / _ \ '__|
  ____) | (__| | | (_| | |_) | |_) |  __/ |   
 |_____/ \___|_|  \__,_| .__/| .__/ \___|_|   
                       | |   | |              
                       |_|   |_| https://github.com/SirRiuz/Scrapper              

'''

print(banner)


try:
    Hyper().addItem(sys.argv[1])
    Request().onRequest()
except Exception:
    print('[E] Falta la url de argumento ...')















