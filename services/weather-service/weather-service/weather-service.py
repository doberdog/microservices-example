"""
The WeatherService invokes a web API to provide data about the weather
"""

from requester import WebAPIRequester

from shared.messaging.rabbitmq_broadcaster import RabbitMQBroadcaster
from shared.messaging.rabbitmq_listener import RabbitMQListener
from shared.messaging.rabbitmq_routing_keys import PetrichorRoutingKeys
from .settings import WEATHER_API_URL


class WeatherService:
    def __init__(self):
        self.requester = WebAPIRequester.for_url(WEATHER_API_URL)
        self.broadcaster = RabbitMQBroadcaster()
        self.listener = RabbitMQListener(routing_key=PetrichorRoutingKeys.WEATHER_SERVICE)

    def run(self):
        self.listener.consume(self.handle_request)

    def handle_request(self):
        pass
