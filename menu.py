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

    contact =     {
        "first_name": "",
        "last_name": "",
        "phone_number": "",
        "email_address": ""
    }

    print("Please enter the following details for the contact you would like to add:")
    contact["first_name"] = input("First Name: ")
    contact["last_name"] = input("Last Name: ")
    contact["phone_number"] = input("Phone Number: ")
    contact["email_address"] = input("Email Address: ")
    
    add_contact(contact)

def option_3():

    print("How would you like to search for contact?")

    print("1. First Name")
    print("2. Last Name")
    print("3. Phone Number")
    print("4. Email Address")

    search_option = int(input())

    search_value = input("Please enter the value you would like to search for? ")

    found_contact = search_contact(search_option, search_value)

    if found_contact:
        print("Found Contact:")
        display_contact(found_contact)
    else:
        print("Contact not found")

def option_4():
    # delete_contact():
   print("delete_contact()")

