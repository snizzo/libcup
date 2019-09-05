from datetime import datetime, date, timedelta

'''
Static class used to do datetime<->string conversion.
'''

class DateConverter:
    def __init__(self):
        pass
    
    @staticmethod
    def today():
        return datetime.today()

    '''
    Converts a libcup formatted string to a datetime to be used
    in apicalls
    @param day string
    @param seconds additional seconds, will be converted into hours/minutes
    '''
    @staticmethod
    def fromStringToDate(day, secs=None):
        if secs == None:
            date = datetime.strptime(day, "%Y-%m-%d")
        else:
            delta = timedelta(seconds=secs)
            date = datetime.strptime(day,"%Y-%m-%d") + delta
        return date

    @staticmethod
    def fromDateToPrint(date):
        strdate = date.strftime("%Y-%m-%d %H:%M")
        return strdate

    '''
    Converts a datetime to a libcup formatted string to be used
    in apicalls
    '''
    @staticmethod
    def fromDateToString(date):
        strdate = date.strftime("%Y-%m-%d")
        return strdate