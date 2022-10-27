import daskFunctions
import publisher
import consumer
import sys

class ConsumerWorker(consumer.Consumer):
    def callback(self, channel, method, properties, body):
        print(" [x] Received new message %r for %r" % (body, method.routing_key))

        publisher_file = publisher.Publisher({'host': 'localhost', 'port': 5672})
        worker = daskFunctions.DaskFunctions()

        publisher_file.publish('proves', worker.readCSV(body.decode().split(':')[0])+':'+worker.columns()+':'+worker.head(int(body.decode().split(':')[1]))+':'+worker.isin(body.decode().split(':')[2], body.decode().split(':')[3])+':'+worker.item(int(body.decode().split(':')[4]), int(body.decode().split(':')[5]))+':'+worker.max('Temp_max')+':'+worker.min('Temp_min'))

consumer_name = ConsumerWorker({'host':'localhost', 'port':5672}, 'worker'+sys.argv[1], 'worker'+sys.argv[1])
consumer_name.consume()