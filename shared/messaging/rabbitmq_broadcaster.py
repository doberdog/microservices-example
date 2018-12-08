"""
Responsible for composing and broadcasting RabbitMQ messages
"""
import json

import pika


class RabbitBroadcaster:

    def __init__(self, rabbit_connector):
        self.rabbit = rabbit_connector

    def broadcast(self, message, routing_key):
        """
        Serializes and emits a message to a RabbitMQ Exchange
        :param message: SwoopMessage to send to a message exchange
        :param routing_key: the routing key
        """
        serialized_message = json.dumps(message)

        self.rabbit.channel.basic_publish(
                exchange=self.rabbit.exchange,
                routing_key=routing_key,
                body=serialized_message,
                properties=pika.BasicProperties(
                        delivery_mode=2
                )
        )
