import xmlrpc.client
import threading
import sys

def treat_file(client_worker, num_thread, maxs, mins):
    print(client_worker.readCSV(sys.argv[num_thread])+"\n")
    print(client_worker.columns()+"\n")
    print(client_worker.head(5)+"\n")
    print(client_worker.isin('City', 'Tarragona')+"\n")
    print(client_worker.item(5, 3)+"\n")
    maxs.append(float(client_worker.max('Temp_max')))
    mins.append(float(client_worker.min('Temp_min')))

threads=[]
maxs=[]
mins=[]

num_thread=1
while num_thread<len(sys.argv):
    client_master = xmlrpc.client.ServerProxy('http://localhost:9000')
    client_worker = xmlrpc.client.ServerProxy(client_master.listWorkers()[(num_thread-1)%client_master.numWorkers()])
    threads.append(threading.Thread(target=treat_file, name="thread%s" %(num_thread+1), args=(client_worker, num_thread, maxs, mins)))
    threads[num_thread-1].start()
    num_thread+=1

num_thread=1
while num_thread<len(sys.argv):
    threads[num_thread-1].join()
    num_thread+=1

print("Temperatura maxima: "+str(max(maxs)))
print("Temperatura minima: "+str(min(mins)))