import check50
from re import escape, search, sub

def set_today(date):

    # Parse date
    year, month, day = date.split(sep="-", maxsplit=2)
    month = month.lstrip("0")
    day = day.lstrip("0")

    # Substitute testing date object with new date object
    with open("testing.py", "r") as testing_file:
        new_testing_contents = sub(r"return date\(\d{4}, *\d{1,2}, *\d{1,2}\)", fr"return date({year}, {month}, {day})", testing_file.read())

    # Write updated date object to testing file
    with open("testing.py", "w") as testing_file:
        testing_file.write(new_testing_contents)


set_today("2000-01-01")