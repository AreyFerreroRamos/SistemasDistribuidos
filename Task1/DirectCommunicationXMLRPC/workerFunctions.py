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