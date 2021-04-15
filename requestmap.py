

# Libs

from hyperHandler import Hyper
import requests



class Request():

    def onRequest(self):
        try:
            urlRequest = Hyper().getItem()

            if urlRequest != '':
                response = requests.get(urlRequest) 
                print('[I] Conectando a > "{url}"'.format(url=urlRequest))
                if response.status_code == 200:
                    print('Ok reques')
        
                else:
                    print('[E] Request error > {e}'.format(e=request.status_code))

            else:
                print('[E] Ya no hay url en el directorio hyper.link')
                exit()

        except Exception:
            print('[E] A ocurrido un error ...')

        self.onRequest()



#Request().onRequest()





