import pika
import abc

class Consumer(abc.ABC):
    def __init__(self, config, exchange_name, binding_key):
        self.config = config
        self.exchange_name = exchange_name
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

        channel.exchange_declare(exchange=self.exchange_name, exchange_type='direct')
        result = channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue
        channel.queue_bind(exchange=self.exchange_name, queue=queue_name, routing_key=self.binding_key)

        channel.basic_consume(queue=queue_name, on_message_callback=self.callback, auto_ack=True)

        try:
            print(' [*] Waiting for data. Use control + c to exit.\n')
            channel.start_consuming()
        except KeyboardInterrupt:
            print(' [*] Exiting...\n')
            channel.stop_consuming()