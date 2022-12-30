import xmlrpc.client
import time

def ping_nodes(node, port, event):
    if (node.getNodeType() == "master"):
        proxy_master = xmlrpc.client.ServerProxy('http://localhost:'+port, allow_none=True)
    else:
        proxy_worker = xmlrpc.client.ServerProxy('http://localhost:'+port, allow_none=True)
        workers=[]

    while True:
        if event.is_set():
            break
        else:
            if (node.getNodeType() == "master"):
                for worker in proxy_master.listWorkers():
                    try:
                        xmlrpc.client.ServerProxy(worker, allow_none=True).isAlive()
                    except:
                        proxy_master.removeWorker(worker.split(':')[2])
            else:
                try:
                    proxy_master = xmlrpc.client.ServerProxy(proxy_worker.getMaster(), allow_none=True)
                    proxy_master.isAlive()
                    workers = proxy_master.listWorkers()
                except:
                    for worker in workers:
                        proxy = xmlrpc.client.ServerProxy(worker, allow_none=True)
                        isLeader = proxy.canBeLeader(worker.split(':')[2], port)
                        if (isLeader == False):
                            break
                    if (isLeader == True):
                        node.setNodeType("master")
                        workers.remove('http://localhost:'+port)
                        proxy_master = xmlrpc.client.ServerProxy('http://localhost:'+port, allow_none=True)
                        for worker in workers:
                            proxy_master.addWorker(worker)
                            proxy_worker = xmlrpc.client.ServerProxy(worker, allow_none=False)
                            proxy_worker.setMaster('http://localhost:'+port)
        time.sleep(1)