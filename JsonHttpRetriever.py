from SessionedRequest import SessionedRequest

class JsonHttpRetriever:
    def __init__(self):
        self.url = None
        self.rawdata = None
        self.data = None
        self.verbose = False
    
    def setUrl(self, url):
        self.url = url

    def setVerbose(self, v):
        self.verbose = v

    def load(self):
        req = SessionedRequest.get()
        r = req.get(self.url)
        self.rawdata = r.content
        if self.verbose:
            print(self.getRawData())

        self.data = r.json()

        return self.data

    def getRawData(self):
        return self.rawdata

    def getData(self):
        assert self.data!=None, "called getData without loading call first"
        return self.data

    def areThereErrors(self):
        if b"ERRORE" in self.rawdata:
            return True
        else:
            return False
