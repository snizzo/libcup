from JsonHttpRetriever import JsonHttpRetriever
from UrlProvider import UrlProvider
from Hospital import Hospital
from HospitalServiceCode import HospitalServiceCode

'''
TODO: implementare qui la funzionalita di tirare fuori le aziende
che forniscono una certa prestazione
'''

class HospitalsProvider(JsonHttpRetriever):
    def __init__(self):
        JsonHttpRetriever.__init__(self)

    def get(self, code, priority):
        if isinstance(code, HospitalServiceCode):
            code = code.code

        self.setUrl(UrlProvider.estimatedTime(code, priority))
        jsondata = self.load()

        if self.areThereErrors():
            print("CRITICAL: server side error:", self.rawdata)
            return []

        hospitals = []

        for jsonregion in jsondata['aziende']:
            for jsonhospital in jsonregion['sedi']:
                sede = jsonhospital['sede']

                indirizzo = ""
                if 'indirizzo' in sede:
                    indirizzo = sede['indirizzo']
                
                descrizione = ""
                if 'descrizione' in sede:
                    descrizione = sede['descrizione']
                
                comuneProvincia = ""
                if 'comuneProvincia' in sede:
                    comuneProvincia = sede['comuneProvincia']

                h = Hospital()
                h.description = jsonregion['azienda']
                h.id_hospital = jsonhospital['sede']['idStruttura']
                h.address = indirizzo + " " + descrizione + " " + comuneProvincia

                hospitals.append(h)


        return hospitals