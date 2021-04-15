

# Libs

from bscraper import Bs
from hyperHandler import Hyper
import requests


class Request():

    def onRequest(self):
        urlRequest = Hyper().getItem()
        minUrl = urlRequest[:80] + '...'
        try:
            #print('[I] Conectando a > "{url}"'.format(url=urlRequest))

            if urlRequest != '':
                print('\n\n[I] Conectando con => "{url}"'.format(url=minUrl))
                response = requests.get(urlRequest) 

                if response.status_code == 200:
                    print('\n  [✔] 200 {url}'.format(url=minUrl))
                    Bs(response)
        
                else:
                    print('[✖] {code} {url} \n'.format(code=status_code , url=minUrl))
                    #print('[E] Request error => {e}'.format(e=request.status_code))

            else:
                print('\n[E] Ya no hay url en el directorio hyper.link')
                exit()

        except Exception:
            print('\n  [E] A ocurrido un error al conectar con > {url}'.format(url=minUrl))

        self.onRequest()

#Request().onRequest()





