# -*- coding: utf-8 -*-
from dateutil.parser import parse
import requests

def sun_on_date(location, date):
    """Returns sunrise and sunset times based on location and date"""

    sun_api_url = "http://api.geonames.org/timezoneJSON?lat=" + str(location[0]) + \
                  "&lng=" + str(location[1]) + "&date=" + date + "&username=demo"
    # use my name as username, if it does not work with demo
    sun_api_url_response = requests.get(sun_api_url)
    sun_data = sun_api_url_response.json()
    try:
        sunrise = sun_data["dates"][0]["sunrise"][11:16]
        sunset = sun_data["dates"][0]["sunset"][11:16]
        return sunrise, sunset
    except:
        print sun_data["status"]["message"]
        print "Change usarname to my name to make it work"
        return exit()


def make_day(sunrise, sunset, drawing_precision=4):
    """Creates a list rappresentation of the day, █ rappresenting night time and ☼ daytime

    drawing_precision: the higher the better"""

    day = [["█"]*24*drawing_precision]
    sunrise_int = int(sunrise[:2]) * drawing_precision + int(sunrise[3:]) / 60 / drawing_precision
    sunset_int = int(sunset[:2]) * drawing_precision + int(sunset[3:]) / 60 / drawing_precision
    for i in range(sunrise_int, sunset_int):
        day[0][i] = "☼"
    return draw_day(day)


def draw_day(day):
    """Returns the night/day drawing as a string rappresentation"""

    day_drawing = ""
    for i in day:
        for j in i:
            day_drawing += j
    return day_drawing


def valid_location(location):
    """Checks if the location gives lat and lng, asks till valid, returns it."""

    lat_lng_url = "http://maps.googleapis.com/maps/api/geocode/json?address=" + location
    lat_lng_url_response = requests.get(lat_lng_url)
    location_data = lat_lng_url_response.json()
    if location_data["status"] == "OK":
        lat_lng = location_data["results"][0]["geometry"]["location"]
        lat, lng = lat_lng["lat"], lat_lng["lng"]
        return lat, lng
    else:
        new_location = raw_input("Invalid location, please try again. ")
        return valid_location(new_location)


def is_valid_date(date):
    """checks if date is valid, reasks till valid, returns date """

    try:
        parse(date)
        return date
    except:
        new_date = raw_input("Invalid date, try again: YYYY-MM-DD ")
        return is_valid_date(new_date)


def get_user_info():
    """Prompts the user for, returns ((lat, lng), date)"""

    user_location = raw_input("Input a location: ")
    user_location = valid_location(user_location)

    user_date = raw_input("What day do you want to know about? \n"
                          "Input a date int the following format: YYYY-MM-DD ")
    user_date = is_valid_date(user_date)

    return user_location, user_date

def play_here():
    """Function that runs the program if it to be run from this file"""

    user_location, user_date = get_user_info()
    sunrise, sunset = sun_on_date(user_location, user_date)
    day = make_day(sunrise, sunset)
    day_drawing = draw_day(day)
    return day_drawing

print play_here()
