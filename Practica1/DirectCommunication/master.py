from xmlrpc.server import SimpleXMLRPCServer
import logging
import os

master = SimpleXMLRPCServer(('localhost', 9000), logRequests=True)
logging.basicConfig(level=logging.INFO)

class WorkerFunctions:
    workers=[]

    def addWorker(self, worker):
        self.workers.append(worker)
        return ' '

    def listWorkers(self):
        return list(self.workers)

    def numWorkers(self):
        return len(self.workers)

    def removeWorker(self, port):
        for worker in self.workers:
            if port==worker.split(':')[2]:
                self.workers.remove(worker)
        return ' '

master.register_instance(WorkerFunctions())

try:
    print('Use control + c to exit the Master node')
    master.serve_forever()
except KeyboardInterrupt:
    print('Exiting master node')