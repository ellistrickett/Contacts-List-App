# contact_manager.py - Contact Manager Module
# Responsible for maintaining and modifying the contact list
import json

# from contact import get_full_name

contact_list = []

def initialise_contact_list(): 
    file = open('contact_list.json')

    for i in json.load(file):
        contact_list.append(i)
        
    file.close()

def write_contact_list_to_file():

    with open("contact_list.json", "w") as file:
        json.dump(contact_list, file)

def add_contact(contact):
    contact_list.append(contact)

    return contact_list

def get_contacts():
    
    return contact_list

def get_contact_by_id(id):

    found_contact = {}

    for contact in contact_list:
        if contact["id"] == id:
            found_contact = contact
    
    return found_contact

def search_contact(query):

    found_contact = {}

    for contact in contact_list:
        if contact["first_name"] == query:
            found_contact = contact
        elif contact["last_name"] == query:
            found_contact = contact
        elif contact["phone_number"] == query:
            found_contact = contact
        elif contact["email_address"] == query:
            found_contact = contact

    return found_contact

def delete_contact(contact):

    contact_list.remove(contact)

def edit_contact(edit_contact):

    found_contact = get_contact_by_id(edit_contact["id"])

    if found_contact:
        delete_contact(found_contact)

        add_contact(edit_contact)