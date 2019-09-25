from libcup import CUP
from DateConverter import DateConverter
from FilterList import FilterList
from DateFilter import DateFilter

import argparse

import sys

desctext = "Fast and efficient hospital booker."

parser = argparse.ArgumentParser(description=desctext)
parser.add_argument("--service", "-s", help="Look for hospital service code")
parser.add_argument("--hospital", "-ho", help="Look for hospital code", action="store_true")
parser.add_argument("--book", "-b", help="Look for bookable appointments within a time rage of 1 week", action="store_true")
parser.add_argument("--servicecode", "-sc", help="Service code")
parser.add_argument("--hospitalcode", "-hc", help="Hospital code")
parser.add_argument("--ssn", "-ssn", help="Social security number")
parser.add_argument("--priority", "-p", help="Service priority")

args = parser.parse_args()

#creating libcup object
c = CUP()

#fastcup.py --service ecografia
if args.service:
    codes = c.getHospitalServiceCodes(args.service)

    for code in codes:
        print(code)

#fastcup.py --hospital --servicecode P395 --priority P
if args.hospital:
    hospitals = c.getHospitals(args.servicecode, args.priority)

    for hospital in hospitals:
        print(hospital)

#python fastcup.py --book --servicecode P3039 --priority D --hospitalcode 30063 --ssn <AAABBB12X34Y567Z>
if args.book:
    services = c.getHospitalServices(args.servicecode,args.priority,args.hospitalcode,args.ssn)

    fl = FilterList(services)
    f = DateFilter()
    f.setGreaterThan(DateConverter.today())
    f.setSmallerThan(DateConverter.today()+DateConverter.delta(7))
    fl.addFilter(f)
    results = fl.getFiltered()

    for result in results:
        print(result)




