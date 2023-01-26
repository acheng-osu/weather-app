from search_by_city import search_by_city
from search_by_zip import search_by_zip

def search():
    while True:
        choice = input("Please choose to either 1) Search by City Name or 2) Search by Zip Code: ")

        if choice == 1:
            pass
        elif choice == 2:
            pass
        else:
            print("That is not one of the options. Please input 1 to search by city name or 2 to search by zip code.")