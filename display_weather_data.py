import datetime
from geopy.geocoders import Nominatim


def display_weather_data(data_dict):
    print("-------------------------------------------------")
    print("location: " +
          str(zip_code_from_coords(data_dict["coord"]["lat"], data_dict["coord"]["lon"])))
    print("coordinates: " +
          str(data_dict["coord"]["lon"]) + "," + str(data_dict["coord"]["lat"]))
    print("weather description: " + data_dict["weather"][0]["description"])
    print("temperature (F): " + str(data_dict["main"]["temp"]))
    print("humidity (%): " + str(data_dict["main"]["humidity"]))
    print("visibility (in meters, max is 10000): " +
          str(data_dict["visibility"]))
    print("wind speed (mph): " + str(data_dict["wind"]["speed"]))
    print("cloudiness (%): " + str(data_dict["clouds"]["all"]))
    print("cloudiness (%): " + str(data_dict["clouds"]["all"]))
    print("sunrise: " + timestamp_to_string(data_dict["sys"]["sunrise"]))
    print("sunset: " + timestamp_to_string(data_dict["sys"]["sunset"]))
    print("-------------------------------------------------")


def timestamp_to_string(secs):
    date_time = datetime.datetime.fromtimestamp(secs)
    date_string = date_time.strftime("%H:%M:%S")
    return date_string


def zip_code_from_coords(lat, lon):
    geolocator = Nominatim(user_agent='weather-app')
    location = geolocator.reverse((lat, lon))
    if 'address' in location.raw.keys():
        if 'postcode' in location.raw['address'].keys():
            return location.raw['address']['town'], location.raw['address']['state'], location.raw['address']['postcode']
    else:
        None
