import requests

class SessionedRequest:
    req = requests.Session()

    '''
    Request has to be sessioned before asking server
    for useful data. Only once per use needed. 
    '''
    isSessioned = False

    @staticmethod
    def get():
        if not SessionedRequest.isSessioned:
            SessionedRequest.req.get('https://servizionline.sanita.fvg.it/prenotazioni')
            SessionedRequest.isSessioned = True

        return SessionedRequest.req