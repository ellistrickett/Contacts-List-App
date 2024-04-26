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
    return True

def get_contacts():
    
    return contact_list

def search_contact(query):
    # for i in contact_list:
    #     if (i["first_name"] == 'Ellis'):
    #         print(i["first_name"])

    return True

def delete_contact(contact):
    return True