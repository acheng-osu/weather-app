from main_menu import display_main_menu
from help_menu import display_help_menu
from search import search
from area_search_by_zip import area_search
from display_weather_data import display_weather_data

def main():
    display_main_menu()
    
    while True:
        user_choice = input("Make your selection: ").lower().strip()

        if user_choice == "s":
            display_weather_data(search())
        elif user_choice == "h":
            display_help_menu()
        elif user_choice == "m":
            display_main_menu()
        elif user_choice == "a":
            area_search_output = area_search()
            print("response from Raymond's microservice: " + str(area_search_output[1]))
            print(area_search_output[0])
        elif user_choice == "x":
            break
        else:
            continue

if __name__ == "__main__":
    main()