from requester import WebAPIRequester

class TestWebAPIRequester:
    def test_static_factory_constructs_instance(self):
        sut = WebAPIRequester.for_url("http://foo.bar")
