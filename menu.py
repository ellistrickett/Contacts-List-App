# menu.py - Menu Module
# Responsible for displaying and implementing the menu options

from contact_manager import get_contacts, add_contact, search_contact, delete_contact

from contact import display_contact, input_contact

def display_menu():
    print("1. Display Contacts")
    print("2. Add Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Quit")

def option_1():
    contacts_list = get_contacts()

    for index, contact in enumerate(contacts_list, start=1):
        print("Contact", index)
        display_contact(contact)

def option_2():

    contact = input_contact()
    
    add_contact(contact)

def option_3(query):

    found_contact = search_contact(query)

    if found_contact:
        print("Found Contact:")
        display_contact(found_contact)
    else:
        print("Contact not found")

def option_4(query):

    found_contact = search_contact(query)

    if found_contact:
        delete_contact(found_contact)
        print("Contact has been deleted")
    else:
        print("Unable to find contact")

def display_search_menu():

    print("How would you like to search for the contact?")

    print("1. First Name")
    print("2. Last Name")
    print("3. Phone Number")
    print("4. Email Address")



