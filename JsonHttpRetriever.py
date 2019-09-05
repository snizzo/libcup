from SessionedRequest import SessionedRequest
    

class JsonHttpRetriever:
    def __init__(self):
        self.url = None
    
    def setUrl(self, url):
        self.url = url

    def load(self):
        req = SessionedRequest.get()
        r = req.get(self.url)
        return r.json()