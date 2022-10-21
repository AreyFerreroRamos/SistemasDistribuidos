import publisher
import sys
        
publisher_name = publisher.Publisher({'host': 'localhost', 'port': 5672})

#maxs=[]
#mins=[]

i=1
while i<len(sys.argv):
    publisher_name.publish('worker'+str(i), sys.argv[i])
    i+=1