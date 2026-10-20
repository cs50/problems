"""
Runs bitcoin.py with a simulated CoinCap API.

Usage: python3 testing.py PRICE [ARGS...]

PRICE is the value of "priceUsd" in the simulated API response. Any remaining
ARGS are passed through to bitcoin.py as its command-line arguments, so from
bitcoin.py's perspective it was run as: python3 bitcoin.py [ARGS...]
"""

import ast
import importlib.util
import json
import sys

import requests
from requests.structures import CaseInsensitiveDict

# Pull the simulated price off the command line so bitcoin.py never sees it
price = sys.argv.pop(1)
sys.argv[0] = "bitcoin.py"

DATA = {
    "data": {
        "id": "bitcoin",
        "rank": "1",
        "symbol": "BTC",
        "name": "Bitcoin",
        "supply": "19823321.0000000000000000",
        "maxSupply": "21000000.0000000000000000",
        "marketCapUsd": "1939613325892.4607145113457500",
        "volumeUsd24Hr": "12341417371.3505338276601668",
        "priceUsd": price,
        "changePercent24Hr": "1.4324165997531723",
        "vwap24Hr": "96203.8859537212418977",
        "explorer": "https://blockchain.info/",
    },
    "timestamp": 1739399343596,
}


class FakeResponse:
    """Mimics the parts of requests.Response that bitcoin.py might use"""

    def __init__(self):
        self.status_code = 200
        self.ok = True
        self.headers = CaseInsensitiveDict({"Content-Type": "application/json"})
        self.text = json.dumps(DATA)
        self.content = self.text.encode()

    def json(self, *args, **kwargs):
        return json.loads(self.text)

    def raise_for_status(self):
        pass


def fake_get(*args, **kwargs):
    return FakeResponse()


def fake_request(method, *args, **kwargs):
    """Stand-in for requests.request: simulate GETs, pass anything else through"""
    if method.upper() == "GET":
        return FakeResponse()
    return real_request(method, *args, **kwargs)


def fake_session_request(self, method, *args, **kwargs):
    """Stand-in for requests.Session.request: simulate GETs, pass anything else through"""
    if method.upper() == "GET":
        return FakeResponse()
    # Delegate to the original Session.request, not requests.request, since the
    # latter calls Session.request internally and would loop back here forever
    return real_session_request(self, method, *args, **kwargs)


# Intercept GET requests made via requests.get, requests.request, or a Session
real_request = requests.request
real_session_request = requests.Session.request
requests.get = fake_get
requests.request = fake_request
requests.Session.get = lambda self, *args, **kwargs: FakeResponse()
requests.Session.request = fake_session_request

with open("bitcoin.py", "r") as f:
    source = f.read()
tree = ast.parse(source)

# Find the if __name__ == "__main__" block
main_guard_node = None
for node in ast.walk(tree):
    if isinstance(node, ast.If):
        # Check if this is the __name__ == "__main__" pattern
        if (isinstance(node.test, ast.Compare) and
            isinstance(node.test.left, ast.Name) and
            node.test.left.id == "__name__" and
            len(node.test.ops) == 1 and
            isinstance(node.test.ops[0], ast.Eq) and
            len(node.test.comparators) == 1 and
            isinstance(node.test.comparators[0], ast.Constant) and
                node.test.comparators[0].value == "__main__"):
            main_guard_node = node
            break

# Load and execute the module
spec = importlib.util.spec_from_file_location("bitcoin", "bitcoin.py")
bitcoin = importlib.util.module_from_spec(spec)
sys.modules["bitcoin"] = bitcoin

# If there's a main guard, we need to handle it specially
if main_guard_node:
    # Create a modified AST that excludes the if __name__ == "__main__" block
    # This prevents the guarded code from running during import
    modified_tree = ast.Module(body=[], type_ignores=[])
    for node in tree.body:
        if node != main_guard_node:
            modified_tree.body.append(node)

    # Compile and execute the modified module (without the main guard)
    code = compile(modified_tree, "bitcoin.py", "exec")
    exec(code, bitcoin.__dict__)

    # Now execute the code that was inside the main guard
    # Create a new module with just the guarded code
    guarded_code = ast.Module(body=main_guard_node.body, type_ignores=[])
    code = compile(guarded_code, "<main_guard>", "exec")
    exec(code, bitcoin.__dict__)
else:
    # No main guard, just execute normally
    spec.loader.exec_module(bitcoin)
