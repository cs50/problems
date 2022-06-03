from datetime import date
import seasons

# Create subclass of date class with patched method, today
class mockDate(date):
    def today():
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

# Run student program
seasons.main()
