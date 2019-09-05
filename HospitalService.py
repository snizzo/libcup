from DateConverter import DateConverter
'''
Data class containing
'''

class HospitalService:
    def __init__(self):
        self.pcode = ""
        self.pdate = ""
        self.phospital = ""
        self.pid_hospital = ""
        self.punit = ""
        self.pid_unit = ""
    
    @property
    def code(self):
        return self.pcode
    
    @code.setter
    def setcode(self, code):
        self.pcode = code
    
    @property
    def date(self):
        return self.pdate
    
    @date.setter
    def setdate(self, date):
        self.pdate = date
    
    @property
    def hospital(self):
        return self.phospital
    
    @hospital.setter
    def sethospital(self, hospital):
        self.phospital = hospital
    
    @property
    def id_hospital(self):
        return self.pid_hospital
    
    @id_hospital.setter
    def setid_hospital(self, id_hospital):
        self.pid_hospital = id_hospital
    
    @property
    def unit(self):
        return self.punit
    
    @unit.setter
    def setunit(self, unit):
        self.punit = unit
    
    @property
    def id_unit(self):
        return self.pid_unit
    
    @id_unit.setter
    def setid_unit(self, id_unit):
        self.pid_unit = id_unit

    def __str__(self):
        out =  "---Hospital Service---" + "\n"
        out += "code:\t\t" + self.code + "\n"
        out += "hospital:\t" + self.hospital + "\n"
        out += "date:\t\t" + DateConverter.fromDateToPrint(self.date) + "\n"
        out += "id_hospital:\t" + str(self.id_hospital) + "\n"
        out += "unit:\t\t" + self.unit + "\n"
        out +=   "id_unit:\t" + str(self.id_unit) + "\n"
        out += "----------------------"
        return out