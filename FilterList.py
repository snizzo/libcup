'''
Filtered object list that accepts starting data and
custom conditions
'''

class FilterList:
    def __init__(self, items=None):
        self.items = None
        self.filtereditems = []

        self.filters = []

        self.setItems(items)
    
    def setItems(self, items):
        if not isinstance(items, list):
            return
        
        self.items = items[:]
        self.filtereditems = items[:]
    
    def hasItems(self):
        return False if self.items == None else True
    
    def getItems(self):
        return self.items
    
    def addFilter(self, filter):
        self.filters.append(filter)

    def getFiltered(self):
        self.filtereditems = []
        for filter in self.filters:
            for item in self.items:
                if filter.apply(item):
                    self.filtereditems.append(item)
        return self.filtereditems