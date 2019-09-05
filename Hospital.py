'''
Data class representing a hospital capable of
delivering certain hospital services.
'''

class Hospital:
    def __init__(self):
        self.paddress = ""
        self.pid_hospital = ""
        self.pdescription = ""
    
    @property
    def address(self):
        return self.paddress
    
    @address.setter
    def setaddress(self, address):
        self.paddress = address
    
    @property
    def description(self):
        return self.description
    
    @description.setter
    def setdescription(self, description):
        self.pdescription = description
    
    @property
    def id_hospital(self):
        return self.pid_hospital
    
    @id_hospital.setter
    def setid_hospital(self, id_hospital):
        self.pid_hospital = id_hospital
    
    def __str__(self):
        out = "---HOSPITAL---\n"
        out +="address:\t" + self.address.encode('utf-8') +"\n"
        out +="id_hospital:\t" + str(self.id_hospital) +"\n"
        out +="description:\t" + self.description.encode('utf-8') +"\n"

        return out