import xmlrpc.client
import threading
import sys
import masterManagerFunctions

def treat_file(client_worker, i, maxs, mins):
    print(client_worker.readCSV(sys.argv[i])+"\n")
    print(client_worker.columns()+"\n")
    print(client_worker.head(5)+"\n")
    print(client_worker.isin('City', 'Tarragona')+"\n")
    print(client_worker.item(5, 3)+"\n")
    maxs.append(float(client_worker.max('Temp_max')))
    mins.append(float(client_worker.min('Temp_min')))
 
client_master = xmlrpc.client.ServerProxy(masterManagerFunctions.MasterManagerFunctions().getMaster())

threads=[]
maxs=[]
mins=[]

i=1
while i<len(sys.argv):
    num_worker=0
    while num_worker<client_master.numWorkers() and i<len(sys.argv):
        worker = client_master.getWorker()
        client_worker = xmlrpc.client.ServerProxy(worker)
        threads.append(threading.Thread(target=treat_file, name="thread%s" %i, args=(client_worker, i, maxs, mins)))
        threads[num_worker].start()
        client_master.addWorker(worker)
        num_worker+=1
        i+=1
    num_worker=0
    while num_worker<len(threads):
        threads[num_worker].join()
        num_worker+=1
    threads.clear()

print("Temperatura maxima: "+str(max(maxs)))
print("Temperatura minima: "+str(min(mins)))