import json
from urllib.parse import urljoin
import requests


class WebAPIRequester:
    def __init__(self, api_key):
        self.url = None
        self.api_key = api_key

    @staticmethod
    def for_url(url, api_key):
        web_req = WebAPIRequester(api_key)
        web_req.url = url
        return web_req

    def get(self, resource):
        endpoint = urljoin(self.url, resource) + "&appid=" + self.api_key
        response = requests.get(endpoint)
        print(json.loads(response))
