import requests
import sys
import importlib.util
import ast
import types


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


def fake_request(method, url, **kwargs):
    if method == "GET":
        return FakeResponse()
    else:
        return requests.request(method, url, **kwargs)


requests.get = lambda *args, **kwargs: FakeResponse()
requests.request = fake_request

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
sys.modules['bitcoin'] = bitcoin

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
