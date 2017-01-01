import daydrawing

print 1
class DayImageOnDate(object):
    """DayImageOnDate has a location and a date, and can create an image of the day based on them"""

    drawing_precision = 4

    def __init__(self, location, date, drawing_precision):

        self.location_lat_lng = daydrawing.valid_location(location)
        self.date = daydrawing.is_valid_date(date)
        self.drawing_precision = drawing_precision
        self.sunrise, self.sunset = daydrawing.sun_on_date(self.location_lat_lng, self.date)

    def make_drawing(self):
        self.drawing = daydrawing.make_day(self.sunrise, self.sunset, self.drawing_precision)
        return self.drawing

# my = DayImageOnDate("koper", "2000-06-11")
# my.drawing_precision = 5
# print my.make_drawing()


def compare_locations(locations, date, drawing_precision=4):
    """Takes a list of locations, and outputs the results for the daydrawings for the location on the various days"""

    location_drawings = []
    for loc in locations:
        drawing = DayImageOnDate(loc, date, drawing_precision).make_drawing()
        drawing += "    " + loc + " on " + date + "\n"
        location_drawings.append(drawing)

    return "".join(location_drawings)


def compare_dates(location, dates, drawing_precision=4):
    """Takes a list of dates and a location, and outputs the daydrawings for the location on the various days"""

    date_drawings = []
    for date in dates:
        drawing = DayImageOnDate(location, date, drawing_precision).make_drawing()
        drawing += "    " + location + " on " + date + "\n"
        date_drawings.append(drawing)

    return "".join(date_drawings)


locations = ["piran", "warwick", "quito"]
# print compare_locations(locations, "2016-04-22")
dates = ["2015-12-20", "2015-06-21"]
#print compare_dates("quito", dates, 6)
