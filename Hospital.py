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
    def address(self, address):
        self.paddress = address
    
    @property
    def description(self):
        return self.pdescription
    
    @description.setter
    def description(self, description):
        self.pdescription = description
    
    @property
    def id_hospital(self):
        return self.pid_hospital
    
    @id_hospital.setter
    def id_hospital(self, id_hospital):
        self.pid_hospital = id_hospital
    
    def __str__(self):
        out = "---HOSPITAL---\n"
        out +="address:\t" + self.address +"\n"
        out +="id_hospital:\t" + str(self.id_hospital) +"\n"
        out +="description:\t" + self.description +"\n"

        return out