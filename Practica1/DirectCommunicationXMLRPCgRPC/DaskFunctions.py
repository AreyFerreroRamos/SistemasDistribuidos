import pandas

class DaskFunctions:   
    def __init__(self):
        self.df = None

    def readCSV(self, name_file):
        self.df = pandas.read_csv(name_file)
        return str(self.df)
    
    def max(self, field):
        return self.df.loc[:,field].max()

    def min(self, field):
        return self.df.loc[:,field].min()

daskFunctions = DaskFunctions()