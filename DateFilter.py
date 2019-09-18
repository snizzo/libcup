from CustomFilter import CustomFilter

'''
used to filter date items
'''

class DateFilter(CustomFilter):
    def __init__(self, greaterThen=None, smallerThen=None, equalTo=None):
        CustomFilter.__init__(self, "date")
