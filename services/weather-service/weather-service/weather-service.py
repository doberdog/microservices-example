"""
The WeatherService invokes a web API to provide data about the weather
"""
from .settings import WEATHER_API_URL


class WeatherService:
    def __init__(self):
        self.requester = WebAPIRequester.for_url(WEATHER_API_URL)
        self.broadcaster = RabbitMQBroadcaster()
        self.listener = RabbitMQListener(routing_key=PetrichorRoutingKeys.WEATHER_SERVICE)

    def run(self):
        self.listener.consume(self.handle_request)

    @staticmethod
    def handle_request():
        print("weather service received request!")


if __name__ == "__main__":
    service = WeatherService()
    service.run()
