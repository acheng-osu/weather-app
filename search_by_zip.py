import requests, json

GEO_URL = "http://api.openweathermap.org/geo/1.0/zip?zip="
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather?lat="
COUNTRY_CODE = "US"
API_KEY = "3db696f6d531856a3aa61c7c32ea1174"

def search_by_zip(zip_code):
    geo_full_url = GEO_URL + str(zip_code) + "," + COUNTRY_CODE + "&appid=" + API_KEY
    geo_response = requests.get(geo_full_url)

    if geo_response.status_code == 200:
        data = geo_response.json()
        coordinates = (data["lat"], data["lon"])

        one_call_full_url = WEATHER_URL + str(coordinates[0]) + "&lon=" + str(coordinates[1]) + "&appid=" + API_KEY + "&units=imperial"
        print(one_call_full_url)
        one_call_response = requests.get(one_call_full_url)

        if one_call_response.status_code == 200:
            data = one_call_response.json()
            return(data)     
        else:
            print("Error in One Call HTTP request with code: " + str(one_call_response.status_code))

    else:
        print("Error in Geo HTTP request with code: " + str(geo_response.status_code))


print(search_by_zip(92354))

