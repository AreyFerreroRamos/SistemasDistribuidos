import pandas

class DaskFunctions:
    def readCSV(self, name_file):
        self.df = pandas.read_csv(name_file)
        return str(self.df)
    
    def max(self, name_file, field):
        self.df = pandas.read_csv(name_file)
        return self.df.loc[:,field].max()

    def min(self, name_file, field):
        self.df = pandas.read_csv(name_file)
        return self.df.loc[:,field].min()