# contacts_main.py - Main Module
# Responsible for displaying the menu and accepting user choices

from tkinter import *

from menu import Menu

from contact_manager import ContactManager

class ContactsMain:
    def __init__(self):
        self.contact_manager = ContactManager()

    def run(self):
        self.contact_manager.initialise_contact_list()

        root = Tk()
        myGUI = Menu(root, self.contact_manager)
        root.mainloop()

        self.contact_manager.write_contact_list_to_file()

if __name__ == "__main__":
    main = ContactsMain()
    main.run()
