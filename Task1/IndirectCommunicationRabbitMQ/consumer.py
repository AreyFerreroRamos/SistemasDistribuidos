import pika
import abc

class Consumer(abc.ABC):
    def __init__(self, config, queue_name, binding_key):
        self.config = config
        self.queue_name = queue_name
        self.binding_key = binding_key
        self.connection = self.create_connection()

    def __del__(self):
        self.connection.close()

    def create_connection(self):
        return pika.BlockingConnection(pika.ConnectionParameters(host=self.config['host'], port=self.config['port']))

    @abc.abstractmethod
    def callback(self, channel, method, properties, body):
        pass

    def consume(self):
        channel = self.connection.channel()

        channel.exchange_declare(exchange='workers', exchange_type='topic')
        channel.queue_declare(queue=self.queue_name, exclusive=True)
        channel.queue_bind(exchange='workers', queue=self.queue_name, routing_key=self.binding_key)

        channel.basic_consume(queue=self.queue_name, on_message_callback=self.callback, auto_ack=True)

        try:
            print(' [*] Waiting for data for '+self.queue_name+'. Use control + c to exit.')
            channel.start_consuming()
        except KeyboardInterrupt:
            print(' [*] Exiting...')
            channel.stop_consuming()