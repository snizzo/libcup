from JsonHttpRetriever import JsonHttpRetriever
from UrlProvider import UrlProvider
from HospitalServiceCode import HospitalServiceCode

class HospitalServiceCodesProvider(JsonHttpRetriever):
    def __init__(self):
        JsonHttpRetriever.__init__(self)

    def get(self, query=""):
        self.setUrl(UrlProvider.hospitalServiceCodes(query))

        json = self.load()

        if self.areThereErrors():
            print("CRITICAL: server side error:", self.rawdata)
            return []

        codes = []

        for jsoncode in json:
            c = HospitalServiceCode()
            c.code = jsoncode['codicePrestazione']
            c.description = jsoncode['descrizione']
            codes.append(c)

        return codes