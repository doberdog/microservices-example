from petrichor_api_tools import requester


class TestWebAPIRequester:
    def test_static_factory_constructs_instance(self):
        url = "http://foo.bar"
        sut = requester.WebAPIRequester.for_url(url=url)
        assert sut.url == "http://foo.bar"
