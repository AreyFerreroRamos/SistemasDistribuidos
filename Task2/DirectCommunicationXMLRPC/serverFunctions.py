import pandas

class ServerFunctions:
    def __init__(self, master):
        self.master = master
        self.workers = []

    def getMaster(self):
        return self.master

    def setMaster(self, master):
        self.master = master

    def addWorker(self, worker):
        self.workers.append(worker)
        return ' '

    def listWorkers(self):
        return list(self.workers)

    def numWorkers(self):
        return len(self.workers)

    def removeWorker(self, port):
        for worker in self.workers:
            if port == worker.split(':')[2]:
                self.workers.remove(worker)
        return ' '

    def isAlive(self):
        return True

    def canBeLeader(self, self_port, candidate_port):
        if int(self_port) <= int(candidate_port):
            return True
        else:
            return False
    
    def readCSV(self, name_file):
        self.df = pandas.read_csv(name_file)
        return str(self.df)

    def apply(self, fields, code):
        return str(self.df[fields].apply(code))

    def columns(self):
        return str(self.df.columns)

    def groupby(self, field):
        return str(self.df.groupby(field))

    def head(self, num_rows):
        return str(self.df.head(num_rows))

    def isin(self, field, element):
        return str((element in self.df[field].values) == True)

    def item(self, row, column):
        return str(self.df.iloc[row, column])

    def items(self):
        return str(self.df.items())

    def max(self, field):
        return str(self.df.loc[:,field].max())

    def min(self, field):
        return str(self.df.loc[:,field].min())