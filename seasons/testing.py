from datetime import date
import seasons


class mockDate(date):
    def today():
        return date(2000, 1, 1)


try:
    seasons.datetime.date = mockDate
except AttributeError:
    seasons.date = mockDate

seasons.main()