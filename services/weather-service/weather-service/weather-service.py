"""
The WeatherService invokes a web API to provide data about the weather
"""

from requester import WebAPIRequester
from .settings import WEATHER_API_URL


class WeatherService:
    def __init__(self):
        self.requester = WebAPIRequester.for_url(WEATHER_API_URL)

    def run(self):
        pass
