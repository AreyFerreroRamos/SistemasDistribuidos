import xmlrpc.client
import threading
import sys

def treat_file(maxs, mins, i):
    client_master = xmlrpc.client.ServerProxy('http://localhost:9000')
    client_worker = xmlrpc.client.ServerProxy(client_master.listWorkers()[(i-1)%client_master.numWorkers()])
    print(client_worker.readCSV(sys.argv[i])+"\n")
    print(client_worker.columns()+"\n")
    print(client_worker.head(5)+"\n")
    print(client_worker.isin('City', 'Tarragona')+"\n")
    print(client_worker.item(5, 3)+"\n")
    maxs.append(float(client_worker.max('Temp_max')))
    mins.append(float(client_worker.min('Temp_min')))

threads=[]
maxs=[]
mins=[]
i=1

while i<len(sys.argv):
    threads.append(threading.Thread(target=treat_file, name="thread%s" %i, args=(maxs, mins, i)))
    threads[i-1].start()
    i+=1

i=1
while i<len(sys.argv):
    threads[i-1].join()
    i+=1

print("Temperatura maxima: "+str(max(maxs)))
print("Temperatura minima: "+str(min(mins)))