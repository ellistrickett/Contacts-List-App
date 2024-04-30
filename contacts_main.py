# contacts_main.py - Main Module
# Responsible for displaying the menu and accepting user choices

from tkinter import *

from menu import display_menu, option_1, option_2, option_3, option_4, display_search_menu, Menu

from contact_manager import initialise_contact_list

def get_user_choice():
        try:
            choice = int(input("Enter your choice: "))
            return choice
        except ValueError:
            print("Invalid input. Please enter a number.")
            return 0

def main():
    
    # main_menu = MainMenu(contact_manager)

    initialise_contact_list()

    root = Tk()
    myGUI = Menu(root)
    root.mainloop()

    while True:
        display_menu()
        choice = get_user_choice()

        if choice == 1:
            option_1()
        elif choice == 2:
            option_2()
        elif choice == 3:
            display_search_menu()
            search_option = get_user_choice()
            search_value = input("Please enter the value you would like to search for? ")
            option_3({ "search_option": search_option, "search_value": search_value})
        elif choice == 4:
            display_search_menu()
            search_option = get_user_choice()
            search_value = input("Please enter the value you would like to search for? ")
            option_4({ "search_option": search_option, "search_value": search_value})
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
