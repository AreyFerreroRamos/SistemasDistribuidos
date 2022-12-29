import redis
import pandas

class ServerFunctions:
    def __init__(self):
        self.redis_cli = redis.Redis(host="localhost", port=16379, decode_responses=True, encoding="utf-8")
    
    def addWorker(self, worker):
        self.redis_cli.rpush('workers', worker)
        return ' '

    def getWorker(self):
        return self.redis_cli.lpop('workers')

    def listWorkers(self):
        return self.redis_cli.lrange('workers', 0, -1)

    def numWorkers(self):
        return self.redis_cli.llen('workers')

    def removeWorker(self, port):
        self.redis_cli.lrem('workers', 0, 'http://localhost:'+port)
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