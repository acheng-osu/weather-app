from search_by_city import search_by_city
from search_by_zip import search_by_zip

def search():
    while True:
        choice = input("Please choose to either 1) Search by City Name or 2) Search by Zip Code: ").strip()

        if choice == "1":
            print("Note: additional steps required if there are multiple cities with the same name")
            city_name = input("Please input the city name: ").strip().title()
            state_code = input("Please input the 2 character state code: ").strip().upper()
            return search_by_city(city_name, state_code)
        elif choice == "2":
            zip_code = input("Please input the 5-digit US zip code: ").strip()
            return search_by_zip(int(zip_code))
        elif choice == "x":
            break
        else:
            print("That is not one of the options. Please input 1 to search by city name or 2 to search by zip code. \
                If you would like to exit the search, input x.")