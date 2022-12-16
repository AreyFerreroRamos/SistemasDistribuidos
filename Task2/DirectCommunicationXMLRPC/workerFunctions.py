import redis
import pandas

class WorkerFunctions:
    redis_cli = redis.Redis(host="localhost", port=16379, decode_responses=True, encoding="utf-8")
    
    def addWorker(self, worker):
        self.redis_cli.rpush('workers', worker)
        return ' '

    def getWorker(self):
        return self.redis_cli.lpop('workers')

    def numWorkers(self):
        return self.redis_cli.llen('workers')

    def removeWorker(self, port):
        self.redis_cli.lrem('workers', 0, 'http://localhost:'+port)
        return ' '
        
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