"""
Exposes functionality for using a RabbitMQ Server
"""

import pika
from pika import BlockingConnection

from petrichor_messaging.settings import RABBIT_HOST, RABBIT_PORT, RABBIT_EXCHANGE, RABBIT_USER, RABBIT_PASS, \
    RABBIT_CONN_MAX_ATTEMPTS, RABBIT_CONN_RETRY_TIMEOUT


class RabbitMQConnection:
    """
    Encapsulates a RabbitMQ Connection
    """
    def __init__(self, host=RABBIT_HOST, port=RABBIT_PORT, exchange=RABBIT_EXCHANGE,
                 user=RABBIT_USER, pword=RABBIT_PASS):
        self.host = host
        self.port = port
        self.exchange = exchange
        self.user = user
        self.pword = pword


class RabbitMQConnector:
    """
    Exposes a connection to a RabbitMQ instance.
    """

    def __init__(self, conn_params=RabbitMQConnection()):
        self.conn_params = conn_params
        self.print_params()

        self.credentials = pika.PlainCredentials(conn_params.user, conn_params.pword)
        self.connection = self.get_rabbit_connection()
        self.channel = self.create_channel()
        self.declare_exchange()

    def create_channel(self):
        print(f"Creating RabbitMQ Channel...")
        try:
            return self.connection.channel()

        except Exception as e:
            print(f"Error creating a RabbitMQ Channel!]")
            print(e)

    def get_rabbit_connection(self):
        """
        Returns a BlockingConnection to a RabbitMQ server with
        the credentials specified in the class ctor
        """
        print(f"Creating RabbitMQ Connection on {self.conn_params.host}:{self.conn_params.port}")

        connection_params = pika.ConnectionParameters(
                host=self.conn_params.host,
                port=self.conn_params.port,
                credentials=self.credentials,
                virtual_host='/',
                heartbeat=0,
                connection_attempts=RABBIT_CONN_MAX_ATTEMPTS,
                retry_delay=RABBIT_CONN_RETRY_TIMEOUT,
                ssl=False,
        )

        return BlockingConnection(connection_params)

    def declare_exchange(self):
        """
        Declares a RabbitMQ exchange
        """
        self.channel.exchange_declare(
                exchange=self.conn_params.exchange,
                exchange_type='direct',
                passive=False,
                durable=True,
                auto_delete=False
        )

    def print_params(self):
        print("Initializing RabbitMQConnector with connection params:")
        for param, value in vars(self.conn_params).items():
            print(f"Param: {param}, Value: {value}")
