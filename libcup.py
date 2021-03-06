from JsonHttpRetriever import JsonHttpRetriever
from HospitalServiceCodesProvider import HospitalServiceCodesProvider
from HospitalsProvider import HospitalsProvider
from HospitalServiceProvider import HospitalServiceProvider

class CUP:
    def __init__(self):
        pass

    def getHospitalServiceCodes(self, query=""):
        '''
        Get all "ricetta rossa" codes for every possible
        service provided by every possible hospital infrastructure
        '''
        hscp = HospitalServiceCodesProvider()
        return hscp.get(query)
    
    def getHospitals(self, code, priority):
        '''
        Get an estimated time for a service provided by any hospital based on priority.
        This can return plain wrong results because current server
        side implemented priority queue is based on patient age
        infered by SSN. (e.g. older patients get earlier access).

        Useful for selecting an approximate result (e.g. desired hospital)
        '''
        hp = HospitalsProvider()
        return hp.get(code, priority)
    
    def getHospitalServices(self, code, priority, hospital, ssn, start_date=None):
        '''
        Returns all available hospital services with the correct time slot based on SSN.
        As opposed to getEstimatedTime, @return ed (HospitalService)s are 
        time slots that are bookable instantly.
        '''
        hsp = HospitalServiceProvider()
        return hsp.get(code, priority, hospital, ssn, start_date)
