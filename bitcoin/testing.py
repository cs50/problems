class FakeResponse:
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
                    "rate_float": 37817.3283,
                }
            }
        }

    # Mock raise_for_status
    def raise_for_status(self):
        pass


import requests

requests.get = lambda x, *args, **kwargs: FakeResponse()
requests.request = lambda x, *args, **kwargs: FakeResponse()

# Run bitcoin via import
import bitcoin

# Run bitcoin's main function if not via import
try:
    import re
    import inspect

    # Get commentless source
    source = re.sub(r"#.*(\n|$)", "", inspect.getsource(bitcoin))
    # Look for __name__ check
    if '__name__ == "__main__":' in source:
        bitcoin.main()
except AttributeError:
    # bitcoin has no main function
    pass
