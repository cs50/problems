import check50
import check50.flask


@check50.check()
def exists(self):
    """application.py exists"""
    check50.exists("application.py")


@check50.check(exists)
def startup(self):
    """application starts up"""
    check50.flask.app().get("/").status(200)


@check50.check(startup)
def has_form(self):
    """has form"""

    if len(form_elements("/")) < 1:
        raise check50.Failure("expected form element")


@check50.check(has_form)
def has_text_fields(self):
    """has one or more text fields"""

    form = form_elements("/")[0]
    if len(form.find_all("textarea")):
        return

    inputs = form.find_all("input")
    types = [
        "date", "datetime-local", "email", "month", "number", "password",
        "search", "tel", "text", "time", "url", "week"
    ]

    if any(e.attrs.get("type") in types for e in inputs):
        return

    raise check50.Failure("expected at least one text input")


@check50.check(has_form)
def has_checkbox_or_radio_buttons(self):
    """has one or more checkboxes or two or more radio buttons"""

    inputs = form_elements("/")[0].find_all("input")
    if len(tuple(filter(lambda e: e.attrs.get("type") == "checkbox", inputs))) < 1 and \
        len(tuple(filter(lambda e: e.attrs.get("type") == "radio", inputs))) < 2:
        raise check50.Failure("expected at least one checkbox or two radio buttons")


@check50.check(has_form)
def has_select_and_options(self):
    """has one or more select menus, each with two or more options"""

    selects = form_elements("/")[0].find_all("select")
    if len(selects) < 1 or \
        any(len(select.find_all("option")) < 2 for select in selects):
        raise check50.Failure("expected one or more select menus, each with two or more options")


def form_elements(route):
    return check50.flask.app().get(route).content().find_all("form")
