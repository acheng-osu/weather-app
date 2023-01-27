from main_menu import display_main_menu
from help_menu import display_help_menu
from search import search

def main():
    display_main_menu()
    
    while True:
        user_choice = input("Make your selection: ")

        if user_choice == "s":
            print(search())
        elif user_choice == "x":
            break
        else:
            continue

if __name__ == "__main__":
    main()