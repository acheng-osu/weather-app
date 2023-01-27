import requests, json
from config import API_KEY

WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather?q="
COUNTRY_CODE = "US"

def search_by_city(city, state):
    one_call_full_url = WEATHER_URL + city + "," + state + "," + COUNTRY_CODE + "&appid=" + API_KEY + "&units=imperial"
    one_call_response = requests.get(one_call_full_url)

    if one_call_response.status_code == 200:
        data = one_call_response.json()
        return(data)     
    else:
        return("Error in One Call HTTP request with code: " + str(one_call_response.status_code))


if __name__ == "__main__":
    print(search_by_city("Loma Linda", "CA"))