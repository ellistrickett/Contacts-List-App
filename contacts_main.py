# contacts_main.py - Main Module
# Responsible for displaying the menu and accepting user choices

from tkinter import *

from contact_manager import ContactManager
from menu import Menu


class ContactsMain:
    # Self represents the ContactsMain object initiaialised
    def __init__(self):
        # When ContactsMain initialised create a ContactManager object
        self.contact_manager = ContactManager()

    # Run method runs program
    def run(self):
        # Call ContactManager initialise_contact_list
        # Read Contacts list from json and hold in ContactManager Object
        self.contact_manager.initialise_contact_list()

        # Top level widget
        root = Tk()
        # Menu that sits in top level widget and allows pop ups etc and will be the GUI
        myGUI = Menu(root, self.contact_manager)
        # Works similar to a while loop that runs Tkinter
        root.mainloop()

        # Call ContactManager write_contact_list_to_file
        # Once app has been closed write contacts to json to save for next time
        self.contact_manager.write_contact_list_to_file()


# Execute the program
if __name__ == "__main__":
    # Initialise ContactsMain
    main = ContactsMain()
    # Execute the run method
    main.run()
