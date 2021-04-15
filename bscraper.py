

from bs4 import BeautifulSoup
from extractlinks import extract


class Bs():

    def __init__(self,HttpObject:object):
        self.__htmlContent = HttpObject.content
        self.__bsObject = BeautifulSoup(self.__htmlContent , 'html.parser')


    def getObject(self) -> (object):
        return self.__bsObject





# Modulos
# bsObject = Bs()
# extract(bsObject.getObject())



