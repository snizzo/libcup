'''
Data class pair code/description representing the abstract
hospital service.
'''

class HospitalServiceCode:
    def __init__(self):
        self.pcode = ""
        self.pdescription = ""
    
    @property
    def code(self):
        return self.pcode
    
    @code.setter
    def code(self, code):
        self.pcode = code
    
    @property
    def description(self):
        return self.pdescription
    
    @description.setter
    def description(self, description):
        self.pdescription = description
    
    def __str__(self):
        out = "<"+ str(self.code) + ": " + self.description + ">"

        return out