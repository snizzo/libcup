from libcup import CUP
from DateConverter import DateConverter
from FilterList import FilterList
from DateFilter import DateFilter
from SessionedRequest import SessionedRequest

import argparse

from notify_run import Notify

import sys, time, json, math

desctext = "Fast and efficient hospital booker."

parser = argparse.ArgumentParser(description=desctext)
parser.add_argument("--service", "-s", help="Look for hospital service code")
parser.add_argument("--hospital", "-ho", help="Look for hospital code", action="store_true")
parser.add_argument("--book", "-b", help="Look for bookable appointments within a time rage of 1 week", action="store_true")
parser.add_argument("--multibook", "-mb", help="Look for bookable appointments from multiple hospitals", action="store_true")
parser.add_argument("--servicecode", "-sc", help="Service code")
parser.add_argument("--hospitalcode", "-hc", help="Hospital code")
parser.add_argument("--ssn", "-ssn", help="Social security number")
parser.add_argument("--priority", "-p", help="Service priority")
parser.add_argument("--notify", "-n", help="Requests a longpoll and periodic notification", action="store_true")
parser.add_argument("--multinotify", "-mn", help="Requests a longpoll and periodic notification on multiple hospitals", action="store_true")
parser.add_argument("--seconds", "-secs", help="Seconds between calls")
parser.add_argument("--desperate", "-d", help="Tries to find the first date as soon as possible, wherever it is possible", action="store_true")

args = parser.parse_args()

#fastcup.py --service ecografia
if args.service:
    c = CUP()
    codes = c.getHospitalServiceCodes(args.service)

    for code in codes:
        print(code)

#fastcup.py --hospital --servicecode P395 --priority P
if args.hospital:
    c = CUP()
    hospitals = c.getHospitals(args.servicecode, args.priority)

    for hospital in hospitals:
        print(hospital)

#python fastcup.py --book --servicecode P3039 --priority D --hospitalcode 30063 --ssn <AAABBB12X34Y567Z>
if args.book:
    c = CUP()
    services = c.getHospitalServices(args.servicecode,args.priority,args.hospitalcode,args.ssn)

    fl = FilterList(services)
    f = DateFilter()
    f.setGreaterThan(DateConverter.today())
    f.setSmallerThan(DateConverter.today()+DateConverter.delta(400))
    fl.addFilter(f)
    results = fl.getFiltered()

    for result in results:
        print(result)

#python fastcup.py --multibook --servicecode P3039 --priority D --hospitalcode 30063,416,35183 --ssn <AAABBB12X34Y567Z>
if args.multibook:
    hospitals = args.hospitalcode.split(",")

    for hospital in hospitals:
        print("fetching timeslots for hospital:"+hospital)
        c = CUP()
        services = c.getHospitalServices(args.servicecode,args.priority,hospital,args.ssn)

        fl = FilterList(services)
        f = DateFilter()
        f.setGreaterThan(DateConverter.today())
        f.setSmallerThan(DateConverter.today()+DateConverter.delta(600))
        fl.addFilter(f)
        results = fl.getFiltered()

        for result in results:
            print(result.hospital)
        time.sleep(2)

#python fastcup.py --notify --servicecode P3039 --priority D --hospitalcode 30063 --ssn <AAABBB12X34Y567Z>
if args.notify:
    notify = Notify()
    qr = notify.register()

    secs = 120
    if args.seconds:
        secs = args.seconds

    print("Please subscribe to this push channel to receive notification directly on your device (pc, phone, ...)")

    print(qr)

    input("Press Enter to continue...")

    while True:
        c = CUP()
        print("fetching timeslots...")
        try:
            services = c.getHospitalServices(args.servicecode,args.priority,args.hospitalcode,args.ssn)
            for s in services:
                print(s)
            
            fl = FilterList(services)
            f = DateFilter()
            f.setGreaterThan(DateConverter.today())
            f.setSmallerThan(DateConverter.today()+DateConverter.delta(7))
            fl.addFilter(f)
            results = fl.getFiltered()

            if len(results)>0:
                notify.send("Appointment found!!")
        except json.decoder.JSONDecodeError:
            print("regenerating session...")
            SessionedRequest.reload()
        
        time.sleep(secs)

#python fastcup.py --multinotify --servicecode P3039 --priority D --hospitalcode 30063,416,35183 --ssn <AAABBB12X34Y567Z>
if args.multinotify:
    notify = Notify()
    qr = notify.register()

    print("Please subscribe to this push channel to receive notification directly on your device (pc, phone, ...)")

    print(qr)

    input("Press Enter to continue...")

    hospitals = args.hospitalcode.split(",")

    #setting time
    secs = 120
    if args.seconds:
        secs = args.seconds

    #time tries to balance between info gathering and not spamming server too much
    #logarithm base 2 of hospitals number
    secs = secs*math.log2(len(hospitals))

    print("time has been automatically set to "+str(secs)+" seconds for refresh due to the number of hospitals: "+str(len(hospitals)))

    while True:
        c = CUP()
        print("fetching timeslots...")
        try:
            for hospital in hospitals:
                print("fetching timeslots for hospital:"+hospital)
                services = c.getHospitalServices(args.servicecode,args.priority,hospital,args.ssn)

                for s in services:
                    print(s)
                
                fl = FilterList(services)
                f = DateFilter()
                f.setGreaterThan(DateConverter.today())
                f.setSmallerThan(DateConverter.today()+DateConverter.delta(7))
                fl.addFilter(f)
                results = fl.getFiltered()

                if len(results)>0:
                    notify.send("Appointment found at hospital:"+result[0].hospital)
                time.sleep(3)
                
        except json.decoder.JSONDecodeError:
            print("regenerating session...")
            SessionedRequest.reload()
        
        time.sleep(secs)


#python fastcup.py --desperate --servicecode P3039 --priority D --ssn <AAABBB12X34Y567Z>
if args.desperate:
    notify = Notify()
    qr = notify.register()

    print("Please subscribe to this push channel to receive notification directly on your device (pc, phone, ...)")

    print(qr)

    input("Press Enter to continue...")

    #getting all the possible hospitals
    mc = CUP()
    hospitals = mc.getHospitals(args.servicecode, args.priority)

    print("found "+str(len(hospitals))+" hospitals offering this service")

    #setting base time
    secs = 120
    if args.seconds:
        secs = args.seconds

    #time tries to balance between info gathering and not spamming server too much
    #logarithm base 2 of hospitals number
    secs = secs*math.log2(len(hospitals))

    print("time has been automatically set to "+str(secs)+" seconds for refresh due to the number of hospitals: "+str(len(hospitals)))

    while True:
        c = CUP()
        print("fetching timeslots...")
        try:
            for hospital in hospitals:
                print("fetching timeslots for hospital:"+str(hospital.id_hospital))
                services = c.getHospitalServices(args.servicecode,args.priority,str(hospital.id_hospital),args.ssn)

                for s in services:
                    print(s)
                
                fl = FilterList(services)
                f = DateFilter()
                f.setGreaterThan(DateConverter.today())
                f.setSmallerThan(DateConverter.today()+DateConverter.delta(7))
                fl.addFilter(f)
                results = fl.getFiltered()

                if len(results)>0:
                    notify.send("Appointment found at hospital:"+result[0].hospital)
                time.sleep(3)
                
        except json.decoder.JSONDecodeError:
            print("regenerating session...")
            SessionedRequest.reload()
        
        time.sleep(secs)


