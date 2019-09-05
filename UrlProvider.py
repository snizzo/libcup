from DateConverter import DateConverter

'''
Provides correct REST-call URLs to be used by other providers.
Useful for centralizing urlcalls in just one class.
Takes care of datetime<->string format conversions.
'''

class UrlProvider:
    raws = {
        'hospitalService':"https://servizionline.sanita.fvg.it/prenotazioni/services/prestazioni?chiaveRicerca=[query]",

        'estimatedTime':"https://servizionline.sanita.fvg.it/prenotazioni/services/tempistimatiattesa?codicePrestazione=[code]&codicePriorita=[priority]",

        'healthServiceAvailability':"https://servizionline.sanita.fvg.it/prenotazioni/services/disponibilita?codicePrestazione=[code]&idSede=[hospital]&codicePriorita=[priority]&dataInizioRicerca=[start_date]&codiceFiscaleAssistito=[ssn]&descrizioneAzienda=[hospital_description]"
    }

    @staticmethod
    def hospitalServiceCodes(query=""):
        url = UrlProvider.raws['hospitalService']
        url = url.replace("[query]", query)
        return url
    
    @staticmethod
    def estimatedTime(code,priority):
        url = UrlProvider.raws['estimatedTime']
        url = url.replace("[code]", code)
        url = url.replace("[priority]", priority)
        return url
    
    @staticmethod
    def healthServiceAvailability(code, priority, hospital, ssn, start_date=None):
        if start_date == None:
            start_date = DateConverter.fromDateToString(DateConverter.today())
        url = UrlProvider.raws['healthServiceAvailability']
        url = url.replace("[code]", code)
        url = url.replace("[priority]", priority)
        url = url.replace("[start_date]", start_date)
        url = url.replace("[hospital]", hospital)
        url = url.replace("[ssn]", ssn)
        url = url.replace("[hospital_description]", '-')
        return url
