# contacts_main.py - Main Module
# Responsible for displaying the menu and accepting user choices

from tkinter import *

from menu import Menu

from contact_manager import initialise_contact_list, write_contact_list_to_file

def main():
    
    # main_menu = MainMenu(contact_manager)

    initialise_contact_list()

    root = Tk()
    myGUI = Menu(root)
    root.mainloop()

    write_contact_list_to_file()

if __name__ == "__main__":
    main()
