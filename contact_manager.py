# contact_manager.py - Contact Manager Module
# Responsible for maintaining and modifying the contact list
import json

from contact import get_full_name

contact_list = []

def initialise_contact_list(): 
    f = open('contact_list.json')

    for i in json.load(f):
        contact_list.append(i)

    f.close()

def add_contact(contact):
    contact_list.append(contact)

    return contact_list

def get_contacts():
    
    return contact_list

# def search_contact(query):
def search_contact(search_option, search_value):

    found_contact = {}

    if search_option == 1:
        for contact in contact_list:
            if contact["first_name"] == search_value:
                found_contact = contact
    elif search_option == 2:
        for contact in contact_list:
            if contact["last_name"] == search_value:
                found_contact = contact
    elif search_option == 3:
        for contact in contact_list:
            if contact["phone_number"] == search_value:
                found_contact = contact
    elif search_option == 4:
        for contact in contact_list:
            if contact["email_address"] == search_value:
                found_contact = contact

    return found_contact

def delete_contact(contact):
    return True