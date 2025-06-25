class FakeResponse:
    def __init__(self):
        self.status_code = 200
        self.text = '{"data":{"id":"bitcoin","rank":"1","symbol":"BTC","name":"Bitcoin","supply":"19823321.0000000000000000","maxSupply":"21000000.0000000000000000","marketCapUsd":"1942459024350.7046787559053215","volumeUsd24Hr":"12485110012.7294932098393723","priceUsd":"97988.5774109547375415","changePercent24Hr":"2.0282219564598007","vwap24Hr":"96203.8859537212418977","explorer":"https://blockchain.info/"},"timestamp":1739400157767}'

    def json(*args):
        return {
            "data": {
                "id": "bitcoin",
                "rank": "1",
                "symbol": "BTC",
                "name": "Bitcoin",
                "supply": "19823321.0000000000000000",
                "maxSupply": "21000000.0000000000000000",
                "marketCapUsd": "1939613325892.4607145113457500",
                "volumeUsd24Hr": "12341417371.3505338276601668",
                "priceUsd": "97845.0243",
                "changePercent24Hr": "1.4324165997531723",
                "vwap24Hr": "96203.8859537212418977",
                "explorer": "https://blockchain.info/"
            },
            "timestamp": 1739399343596
        }

    # Mock raise_for_status
    def raise_for_status(self):
        pass


import requests
requests.get = lambda *args, **kwargs: FakeResponse()

# Run bitcoin via import
import bitcoin

# Run bitcoin's main function if not via import
try:
    bitcoin.main()
except AttributeError:

    # Bitcoin has no main function
    pass
