from main_menu import display_main_menu
from help_menu import display_help_menu
from search import search

def main():
    display_main_menu()
    
    while True:
        user_choice = input("Make your selection: ").lower().strip()

        if user_choice == "s":
            print(search())
        elif user_choice == "h":
            display_help_menu()
        elif user_choice == "m":
            display_main_menu()
        elif user_choice == "x":
            break
        else:
            continue

if __name__ == "__main__":
    main()