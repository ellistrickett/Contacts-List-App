# menu.py - Menu Module
# Responsible for displaying and implementing the menu options

from contact_manager import get_contacts, add_contact, search_contact, delete_contact, contact_list

from contact import display_contact, input_contact

def display_menu():
    print("1. Display Contacts")
    print("2. Add Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Quit")

def display_contacts():
    contacts_list = get_contacts()

    for index, contact in enumerate(contacts_list, start=1):
        print("Contact", index)
        print("First Name:", contact["first_name"]) 
        print("Last Name:", contact["last_name"])
        print("Phone Number:", contact["phone_number"])
        print("Email Address:", contact["email_address"])

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

def option_3():
    # search_contact():
    print("search_contact()")

def option_4():
    # delete_contact():
   print("delete_contact()")

