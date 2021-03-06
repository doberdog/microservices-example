from petrichor_messaging.rabbitmq_connector import RabbitMQConnector


class RabbitMQListener:
    """
    Declares a RabbitMQ Exchange; declares and binds to a RabbitMQ queue
    """

    def __init__(self, routing_key, rabbit_connector=RabbitMQConnector()):
        self.rabbit = rabbit_connector
        self.queue_name = routing_key
        self.routing_key = routing_key

    def consume(self, callback):
        """
        Binds a channel to this queue and starts consuming with the provided callback function
        """
        channel = self.rabbit.channel
        channel.queue_declare(queue=self.queue_name)
        channel.queue_bind(exchange=self.rabbit.conn_params.exchange, queue=self.queue_name)
        channel.basic_consume(callback, queue=self.routing_key, no_ack=True)

        try:
            print(f"Consuming on queue: {self.queue_name}")
            channel.start_consuming()

        except Exception as e:
            print(e)
            channel.stop_consuming()
            self.rabbit.connection.close()

    def connect(self):
        """
        Makes a specific number of connection attempts to a RabbitMQ server
        """
        self.rabbit = RabbitMQConnector()
        print("Connected to RabbitMQ!")
