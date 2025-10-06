from quizgecko import Client, BearerAuth, endpoints

def test_connection():
    client = Client(BearerAuth('YOUR_API_KEY'))
    data = endpoints.languages.list_languages(client)
    assert isinstance(data, dict)
