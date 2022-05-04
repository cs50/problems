class FakeResponse():
    def json(_):
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

    status_code = 200


import requests
requests.get = lambda x : FakeResponse()

# Run bitcoin via import
import bitcoin

# Run bitcoin's main function if not via import
try:
    bitcoin.main()
except AttributeError:

    # Bitcoin has no main function
    pass