import xmlrpc.client
import time

def pingNodes(node, port, event):
    proxy = xmlrpc.client.ServerProxy('http://localhost:'+port, allow_none=True)
    if (node.getNodeType() == "worker"):
        workers=[]

    while True:
        if event.is_set():
            break
        else:
            if (node.getNodeType() == "master"):
                for worker in proxy.listWorkers():
                    try:
                        xmlrpc.client.ServerProxy(worker, allow_none=True).isAlive()
                    except:
                        proxy.removeWorker(worker.split(':')[2])
            else:
                try:
                    proxy_master = xmlrpc.client.ServerProxy(proxy.getMaster(), allow_none=True)
                    proxy_master.isAlive()
                    workers = proxy_master.listWorkers()
                except:
                    for worker in workers:
                        proxy_worker = xmlrpc.client.ServerProxy(worker, allow_none=True)
                        isLeader = proxy_worker.canBeLeader(worker.split(':')[2], port)
                        if (isLeader == False):
                            break
                    if (isLeader == True):
                        node.setNodeType("master")
                        workers.remove('http://localhost:'+port)
                        proxy = xmlrpc.client.ServerProxy('http://localhost:'+port, allow_none=True)
                        for worker in workers:
                            proxy.addWorker(worker)
                            proxy_worker = xmlrpc.client.ServerProxy(worker, allow_none=False)
                            proxy_worker.setMaster('http://localhost:'+port)
        time.sleep(1)