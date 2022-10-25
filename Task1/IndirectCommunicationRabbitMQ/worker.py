import daskFunctions
import pika
import sys

class Consumer:
    def __init__(self, config, queue_name, binding_key):
        self.config = config
        self.queue_name = queue_name
        self.binding_key = binding_key
        self.connection = self.create_connection()

    def __del__(self):
        self.connection.close()

    def create_connection(self):
        return pika.BlockingConnection(pika.ConnectionParameters(host=self.config['host'], port=self.config['port']))

    def callback(self, channel, method, properties, body):
        print(" [x] Received new message %r from %r" % (body, method.routing_key))

        worker = daskFunctions.DaskFunctions()
        message = worker.readCSV(body.decode())
        print('\n'+message+'\n')

    def consume(self):
        channel = self.connection.channel()

        channel.exchange_declare(exchange='proves', exchange_type='topic')
        channel.queue_declare(queue=self.queue_name, exclusive=True)
        channel.queue_bind(exchange='proves', queue=self.queue_name, routing_key=self.binding_key)

        channel.basic_consume(queue=self.queue_name, on_message_callback=self.callback, auto_ack=True)

        try:
            print(' [*] Waiting for data for '+self.queue_name+'. Use control + c to exit the Worker node')
            channel.start_consuming()
        except KeyboardInterrupt:
            print(' [*] Exiting Worker node')
            channel.stop_consuming()

consumer_name = Consumer({'host':'localhost', 'port':5672}, 'worker'+sys.argv[1], 'worker'+sys.argv[1])
consumer_name.consume()