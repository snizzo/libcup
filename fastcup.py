
#from datetime import datetime, timedelta
""" import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify """






from libcup import CUP
from DateConverter import DateConverter
from FilterList import FilterList
from DateFilter import DateFilter

c = CUP()

'''
Get codes for every possible hospital service
'''
codes = c.getHospitalServiceCodes()

#for code in codes:
#    print code

'''
Get all available hospital services
'''
services = c.getHospitalServices("P395","P","30063","DSDCLD92E21E473Y", "2019-09-02")

#for service in services:
#    print service

'''
Hospital service filtering example

fl = FilterList(services)
f = DateFilter()
f.setGreaterThan(DateConverter.today())
f.setSmallerThan(DateConverter.today()+DateConverter.delta(7))
fl.addFilter(f)
print fl.getFiltered()
'''

'''
Get every hospital performing HospitalService with code P395 and priority P
'''
hospitals = c.getHospitals("P395", "P")

#for hospital in hospitals:
#    print hospital






'''
TODO: implement date filter and notification systems

Notify.init("FastCUP")

offerings = json.loads(data.text)

today = datetime.today()

for item in offerings:
    date = item['date'][0]['data']
    datetime = datetime.strptime(date, '%Y-%m-%d')
    
    if datetime-today < timedelta(hours=168):
        desc = description+"Data: "+str(datetime)
        Notify.Notification.new("--- FASTCUP MESSAGGIO URGENTE ---", desc).show()
'''