import redis
import pandas

class DaskFunctions:
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

try:
    print('Use control + c to exit the Worker node')
    redis_cli = redis.Redis(host="localhost", port=16379)
    pubsub = redis_cli.pubsub()
    pubsub.subscribe('read_csv')
    worker = DaskFunctions()
    message = pubsub.get_message('read_csv')
    print(worker.readCSV(message))
except KeyboardInterrupt:
    print('Exiting Worker node')