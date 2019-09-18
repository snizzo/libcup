from SessionedRequest import SessionedRequest
    

class JsonHttpRetriever:
    def __init__(self):
        self.url = None
        self.rawdata = None
        self.data = None
    
    def setUrl(self, url):
        self.url = url

    def load(self):
        req = SessionedRequest.get()
        r = req.get(self.url)
        self.rawdata = r.content
        self.data = r.json()
        return self.data

    def getData(self):
        assert self.data!=None, "called getData without loading call first"
        return self.data

    def areThereErrors(self):
        return "ERRORE" in self.rawdata
