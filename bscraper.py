

from bs4 import BeautifulSoup
from urllib.parse import urlparse
#from extractlinks import extract
from hyperHandler import Hyper



class Bs():

    def __init__(self,HttpObject:object):
        self.__httpObject = HttpObject
        self.__htmlContent = HttpObject.content
        print('  [I] Analizando HTML')
        self.__bsObject = BeautifulSoup(self.__htmlContent , 'html.parser')

        self.extractHyperLinks()

    
    def extractHyperLinks(self):
        print('  [I] Extrayendo hiper vinculos')
        hyperLinks = self.__bsObject.html.find_all('a' , href=True)
        for link in hyperLinks:
            Hyper().addItem(link['href'])





