import requester


class TestWebAPIRequester:
    def test_static_factory_constructs_instance(self):
        sut = requester.WebAPIRequester.for_url(url="http://foo.bar")
