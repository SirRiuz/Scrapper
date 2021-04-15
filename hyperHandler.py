
class Hyper():

    def __init__(self):
        self.fileObject = ''


    def getItem(self) -> (str):
        self.fileObject = open('hyper.link','r')
        urlLine = self.fileObject.readline()
        newFileContent = str(self.fileObject.read()).replace(urlLine,'')
        self.fileObject.close()

        # Eliminando la url de la lista
        self.fileObject = open('hyper.link','w')
        self.fileObject.write(newFileContent)
        self.fileObject.close()

        return str(urlLine).replace('\n','')


    def addItem(self,item:str):
        self.fileObject = open('hyper.link','a')
        self.fileObject.write(item + '\n')
        self.fileObject.close()
        print('[i] Se añadio una url al carchivo:' , item)


#Hyper().addItem("Mayeo")
#print(Hyper().getItem())





