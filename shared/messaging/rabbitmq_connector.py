"""
Exposes functionality for using a RabbitMQ Server
"""
import logging

import pika
from pika import BlockingConnection

from shared.messaging.settings import RABBIT_HOST, RABBIT_PORT, RABBIT_EXCHANGE, RABBIT_USER, RABBIT_PASS, \
    RABBIT_CONN_MAX_ATTEMPTS, RABBIT_CONN_RETRY_TIMEOUT


class RabbitMQConnection:
    """
    Encapsulates a RabbitMQ Connection
    """
    def __init__(self, host=RABBIT_HOST, port=RABBIT_PORT,
                 exchange=RABBIT_EXCHANGE, user=RABBIT_USER,
                 pword=RABBIT_PASS):
        self.host = host
        self.port = port
        self.exchange = exchange
        self.user = user
        self.pword = pword


class RabbitMQConnector:
    """
    Exposes a connection to a RabbitMQ instance.
    """

    def __init__(self, conn=RabbitMQConnection()):
        self.logger = logging.getLogger()
        self.host = conn.host
        self.port = conn.port
        self.credentials = pika.PlainCredentials(conn.user, conn.pword)
        self.exchange = conn.exchange
        self.connection = self.get_rabbit_connection()
        self.channel = self.create_channel()
        self.declare_exchange()

    def create_channel(self):
        try:
            channel = self.connection.channel()
            self.logger.debug(f"Created a RabbitMQ Channel [{channel}]")
            return channel

        except Exception as e:
            self.logger.error(f"Error creating a RabbitMQ Channel!]")
            self.logger.error(e)

    def get_rabbit_connection(self):
        """
        Returns a BlockingConnection to a RabbitMQ server with
        the credentials specified in the class ctor
        """
        connection_params = pika.ConnectionParameters(
                host=self.host,
                port=self.port,
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
                exchange=self.exchange,
                exchange_type='direct',
                passive=False,
                durable=True,
                auto_delete=False
        )
