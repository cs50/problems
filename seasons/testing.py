from datetime import date
import sys
import seasons

# Create subclass of date class with patched method, today
class mockDate(date):
    @classmethod
    def today(cls):
        # Must use 'date' in the return statement for set_today() pattern matching
        # But 'date' here refers to the mockDate class
        date = cls
        return date(2000, 1, 1)


# Override student's import of date class with testing class
seasons.date = mockDate

try:

    # If student has imported datetime module as a whole, override date class inside of datetime module
    seasons.datetime.date = mockDate
except TypeError:

    # Student has instead imported datetime class from datetime module: nothing to do
    pass
except AttributeError:

    # Student has not imported datetime module at all: nothing to do
    pass

# Patch sys.modules to ensure all future imports get the mocked class
# This is necessary for type checks like 'type(x) is date' to work correctly
sys.modules['datetime'].date = mockDate

# Run student program
seasons.main()
