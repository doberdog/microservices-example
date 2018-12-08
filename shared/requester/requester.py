from urllib.parse import urljoin
import requests


class WebAPIRequester:
    def __init__(self):
        self.url = None

    @staticmethod
    def for_url(url):
        web_req = WebAPIRequester()
        web_req.url = url

    def get(self, resource):
        endpoint = urljoin(self.url, resource)
        response = requests.get(endpoint)
