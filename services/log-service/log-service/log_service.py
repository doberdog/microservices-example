"""
The WeatherService invokes a web API to provide data about the weather
"""

from petrichor_api_tools.requester import WebAPIRequester
from petrichor_messaging.rabbitmq_broadcaster import RabbitMQBroadcaster
from petrichor_messaging.rabbitmq_connector import RabbitMQConnector
from petrichor_messaging.rabbitmq_listener import RabbitMQListener
from petrichor_messaging.rabbitmq_routing_keys import PetrichorRoutingKeys


class LogService:
    def __init__(self):
        print("LogService Starting")
        self.requester = WebAPIRequester.for_url('foo')

        self.rabbit_connector = None
        self.broadcaster = None
        self.listener = None

    def run(self):
        self.print_startup_message()
        self.setup_rabbit()
        self.listener.consume(self.handle_request)

    @staticmethod
    def handle_request():
        pass

    @staticmethod
    def print_startup_message():
        print("=======================")
        print("Log Service is started!")
        print("=======================")

    def setup_rabbit(self):
        self.rabbit_connector = RabbitMQConnector()
        self.broadcaster = RabbitMQBroadcaster(self.rabbit_connector)
        self.listener = RabbitMQListener(routing_key=PetrichorRoutingKeys.LOG_SERVICE)


if __name__ == "__main__":
    service = LogService()
    service.run()
