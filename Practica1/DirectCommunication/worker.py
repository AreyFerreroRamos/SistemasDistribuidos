import xmlrpc.client
import sys
import os

from xmlrpc.server import SimpleXMLRPCServer
import logging
import pandas

proxy = xmlrpc.client.ServerProxy('http://localhost:9000')
proxy.addWorker('http://localhost:'+sys.argv[1])

worker = SimpleXMLRPCServer(('localhost', int(sys.argv[1])), logRequests=True)
logging.basicConfig(level=logging.INFO)

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

worker.register_instance(DaskFunctions())

try:
    print('Use control + c to exit the Worker node')
    worker.serve_forever()
except KeyboardInterrupt:
    print('Exiting Worker node')
    proxy.removeWorker(sys.argv[1])