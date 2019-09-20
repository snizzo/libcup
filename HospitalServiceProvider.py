from JsonHttpRetriever import JsonHttpRetriever
from UrlProvider import UrlProvider
from HospitalService import HospitalService
from DateConverter import DateConverter
from Hospital import Hospital
from HospitalServiceCode import HospitalServiceCode

class HospitalServiceProvider(JsonHttpRetriever):
    def __init__(self):
        JsonHttpRetriever.__init__(self)

    def get(self, code, priority, hospital, ssn, start_date):
        if isinstance(code, HospitalServiceCode):
            code = code.code
        
        if isinstance(hospital, Hospital):
            hospital = hospital.id_hospital

        self.setUrl(UrlProvider.healthServiceAvailability(code, priority, hospital, ssn, start_date))

        jsonservices = self.load()

        if self.areThereErrors():
            print("CRITICAL: server side error:", self.rawdata)
            return []

        services = []

        #generating a single service for every possible combination
        for jsonservice in jsonservices:
            for date in jsonservice['date']:
                for orari in date['orari']:
                    s = HospitalService()
                    s.code = code
                    s.hospital = hospital
                    s.date = DateConverter.fromStringToDate(date['data'], orari)
                    s.hospital = jsonservice['sede']['descrizione']
                    s.id_hospital = jsonservice['sede']['idStruttura']
                    s.unit = jsonservice['unitaOfferente']['descrizione']
                    s.id_unit = jsonservice['unitaOfferente']['idStruttura']

                    services.append(s)

        return services