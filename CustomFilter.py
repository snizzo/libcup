'''
used to custom filter data
'''

class CustomFilter:
    def __init__(self, prop):
        '''
        prop -> is the property to be tested inside the filter
        '''
        assert isinstance(prop, str), "filter property must be a string"
        self.prop = prop
        self.greaterThan = None
        self.smallerThan = None
        self.equalTo = None

    def setSmallerThan(self, v):
        self.smallerThan = v
    
    def setGreaterThan(self, v):
        self.greaterThan = v
    
    def setEqualTo(self, v):
        self.equalTo = v
    
    def reset(self):
        self.setConditions(None, None, None)

    def setConditions(self, greaterThan=None, smallerThan=None, equalTo=None):
        self.setGreaterThan(greaterThan)
        self.setSmallerThan(smallerThan)
        self.setEqualTo(equalTo)
    
    def apply(self, item):
        if not hasattr(item, self.prop):
            print "DateFilter: item.", self.prop, " must exists"
            return

        if self.greaterThan!=None:
            if not (getattr(item, self.prop) > self.greaterThan):
                return False
        
        if self.smallerThan!=None:
            if not (getattr(item, self.prop) < self.smallerThan):
                return False
        
        if self.equalTo!=None:
            if not (getattr(item, self.prop) == self.equalTo):
                return False

        return True