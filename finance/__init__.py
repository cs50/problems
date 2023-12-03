import check50
import check50.py
import check50.flask
import os


# Set API_KEY to a dummy value. The distro code looks at this value, but it's not used in checks.
os.environ["API_KEY"] = "foo"


@check50.check()
def exists():
    """app.py exists"""
    check50.exists("app.py")
    check50.include("lookup.py")
    check50.py.append_code("helpers.py", "lookup.py")


@check50.check(exists)
def startup():
    """application starts up"""
    Finance().get("/").status(200)


@check50.check(startup)
def register_page():
    """register page has all required elements"""
    Finance().validate_form("/register", ["username", "password", "confirmation"])


@check50.check(register_page)
def simple_register():
    """registering user succeeds and portfolio page is displayed"""
    Finance().register("_cs50", "ohHai28!", "ohHai28!").status(200)


@check50.check(register_page)
def register_empty_field_fails():
    """registration with an empty field fails"""
    for user in [
        ("", "crimson", "crimson"),
        ("jharvard", "crimson", ""),
        ("jharvard", "", ""),
    ]:
        Finance().register(*user).status(400)


@check50.check(register_page)
def register_password_mismatch_fails():
    """registration with password mismatch fails"""
    Finance().register("check50user1", "thisiscs50", "crimson").status(400)


@check50.check(register_page)
def register_reject_duplicate_username():
    """registration rejects duplicate username"""
    user = ["elfie", "Doggo28!", "Doggo28!"]
    Finance().register(*user).status(200).register(*user).status(400)


@check50.check(startup)
def login_page():
    """login page has all required elements"""
    if Finance().page_exists("/signin"):
        Finance().validate_form("/signin", ["username", "password"])
        return
    Finance().validate_form("/login", ["username", "password"])


@check50.check(simple_register)
def can_login():
    """logging in as registered user succceeds"""
    Finance().login("_cs50", "ohHai28!").status(200).get(
        "/", follow_redirects=False
    ).status(200)


@check50.check(can_login)
def quote_page():
    """quote page has all required elements"""
    Finance().login("_cs50", "ohHai28!").validate_form("/quote", "symbol")


@check50.check(quote_page)
def quote_handles_invalid():
    """quote handles invalid ticker symbol"""
    Finance().login("_cs50", "ohHai28!").quote("ZZZ").status(400)


@check50.check(quote_page)
def quote_handles_blank():
    """quote handles blank ticker symbol"""
    Finance().login("_cs50", "ohHai28!").quote("").status(400)


@check50.check(quote_page)
def quote_handles_valid():
    """quote handles valid ticker symbol"""
    (
        Finance()
        .login("_cs50", "ohHai28!")
        .quote("AAAA")
        .status(200)
        .content(r"28\.00", "28.00", name="body")
    )


@check50.check(can_login)
def buy_page():
    """buy page has all required elements"""
    Finance().login("_cs50", "ohHai28!").validate_form("/buy", ["shares", "symbol"])


@check50.check(buy_page)
def buy_handles_invalid():
    """buy handles invalid ticker symbol"""
    Finance().login("_cs50", "ohHai28!").transaction("/buy", "ZZZZ", "2").status(400)


@check50.check(buy_page)
def buy_handles_incorrect_shares():
    """buy handles fractional, negative, and non-numeric shares"""
    (
        Finance()
        .login("_cs50", "ohHai28!")
        .transaction("/buy", "AAAA", "-1")
        .status(400)
        .transaction("/buy", "AAAA", "1.5")
        .status(400)
        .transaction("/buy", "AAAA", "foo")
        .status(400)
    )


@check50.check(buy_page)
def buy_handles_valid():
    """buy handles valid purchase"""
    (
        Finance()
        .login("_cs50", "ohHai28!")
        .transaction("/buy", "AAAA", "1")
        .transaction("/buy", "AAAA", "3")
        .content(r"112\.00", "112.00")
        .content(r"9,?888\.00", "9,888.00")
    )


@check50.check(buy_handles_valid)
def sell_page():
    """sell page has all required elements"""
    (
        Finance()
        .login("_cs50", "ohHai28!")
        .validate_form("/sell", ["shares"])
        .validate_form("/sell", ["symbol"], field_tag="select")
    )


@check50.check(buy_handles_valid)
def sell_handles_invalid():
    """sell handles invalid number of shares"""
    Finance().login("_cs50", "ohHai28!").transaction("/sell", "AAAA", "8").status(400)


@check50.check(buy_handles_valid)
def sell_handles_valid():
    """sell handles valid sale"""
    (
        Finance()
        .login("_cs50", "ohHai28!")
        .transaction("/sell", "AAAA", "2")
        .content(r"56\.00", "56.00")
        .content(r"9,?944\.00", "9,944.00")
    )


@check50.check(sell_handles_valid)
def history_page():
    """history page shows transactions"""
    (
        Finance()
        .login("_cs50", "ohHai28!")
        .get("/history")
        .content(r"28\.00", "28.00")
        .content("AAAA")
    )


class Finance(check50.flask.app):
    """Extension of flask.App class that adds Finance-specific functions"""

    APP_NAME = "app.py"

    def __init__(self):
        """Helper function for registering user"""
        super().__init__(self.APP_NAME)

    def register(self, username, password, confirmation):
        """Register new user"""
        form = {
            "username": username,
            "password": password,
            "confirmation": confirmation,
        }
        return self.post("/register", data=form)

    def login(self, username, password):
        """Helper function for logging in"""
        route = "/login"
        if self.page_exists("/signin"):
            route = "/signin"
        return self.post(route, data={"username": username, "password": password})

    def quote(self, ticker):
        """Query app for a quote for `ticker`"""
        return self.post("/quote", data={"symbol": ticker})

    def transaction(self, route, symbol, shares):
        """Send request to `route` ("/buy" or "/sell") to perform the relevant transaction"""
        return self.post(route, data={"symbol": symbol, "shares": shares})

    def validate_form(self, route, fields, field_tag="input"):
        """Make sure HTML form at `route` has input fields given by `fields`"""
        if not isinstance(fields, list):
            fields = [fields]

        content = self.get(route).content()
        required = {field: False for field in fields}
        for tag in content.find_all(field_tag):
            try:
                name = tag.attrs["name"]
                if required[name]:
                    raise Error('found more than one field called "{}"'.format(name))
            except KeyError:
                pass
            else:
                check50.log('found required "{}" field'.format(name))
                required[name] = True

        try:
            missing = next(name for name, found in required.items() if not found)
        except StopIteration:
            pass
        else:
            raise check50.Failure(
                f'expected to find {field_tag} field with name "{missing}", but none found'
            )

        if content.find("button", type="submit") is None:
            raise check50.Failure("expected button to submit form, but none was found")

        return self

    def page_exists(self, route):
        return self.get(route).status() == 200
