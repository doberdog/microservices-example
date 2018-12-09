"""
The WeatherService invokes a web API to provide data about the weather
"""
import logging

from petrichor_api_tools.requester import WebAPIRequester
from petrichor_messaging.rabbitmq_broadcaster import RabbitMQBroadcaster
from petrichor_messaging.rabbitmq_connector import RabbitMQConnector
from petrichor_messaging.rabbitmq_listener import RabbitMQListener
from petrichor_messaging.rabbitmq_routing_keys import PetrichorRoutingKeys
from .settings import WEATHER_API_URL


class WeatherService:
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.debug("Weather Service Starting...")

        self.requester = WebAPIRequester.for_url(WEATHER_API_URL)

        self.rabbit_connector = RabbitMQConnector()
        self.broadcaster = RabbitMQBroadcaster(self.rabbit_connector)
        self.listener = RabbitMQListener(routing_key=PetrichorRoutingKeys.WEATHER_SERVICE)

    def run(self):
        self.logger.debug("Weather Service is listening for requests!")
        self.listener.consume(self.handle_request)

    @staticmethod
    def handle_request():
        print("weather service received request!")


if __name__ == "__main__":
    service = WeatherService()
    service.run()
