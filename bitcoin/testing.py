class FakeResponse():

    def __init__(self):
        self.status_code = 200
        self.text = '{"bpi":{"USD":{"code":"USD","symbol": "&#36;","rate":"37,817.3283","description":"United States Dollar","rate_float": 37817.3283}}}'

    def json(*args):
        return {
                "bpi": {
                    "USD": {
                        "code": "USD",
                        "symbol": "&#36;",
                        "rate": "37,817.3283",
                        "description": "United States Dollar",
                        "rate_float": 37817.3283
                    }
                }
            }

import requests
requests.get = lambda x, *args, **kwargs: FakeResponse()

# Run bitcoin via import
import bitcoin

# Run bitcoin's main function if not via import
try:
    bitcoin.main()
except AttributeError:

    # Bitcoin has no main function
    pass