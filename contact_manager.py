# contact_manager.py - Contact Manager Module
# Responsible for maintaining and modifying the contact list
import json
import phonenumbers
import re
from contact import Contact

class ContactManager:
    def __init__(self):
        self.contact_list = []

    def initialise_contact_list(self): 
        file = open('contact_list.json')

        for contact in json.load(file):
            self.contact_list.append(Contact(contact["id"], contact["first_name"], contact["last_name"], contact["phone_number"], contact["email_address"]))
            
        file.close()

    def write_contact_list_to_file(self):

        with open("contact_list.json", "w") as file:
            json.dump(self.contact_list, file, default=vars)

    def add_contact(self, contact):
        self.contact_list.append(contact)

        return self.contact_list

    def get_contacts(self):
        
        return self.contact_list

    def get_contact_by_id(self, id):

        found_contact = {}

        for contact in self.contact_list:
            if contact.id == id:
                found_contact = contact
        
        return found_contact

    def search_contact(self, query):

        found_contact = {}

        for contact in self.contact_list:
            if contact.first_name == query:
                found_contact = contact
            elif contact.last_name== query:
                found_contact = contact
            elif contact.phone_number == query:
                found_contact = contact
            elif contact.email_address == query:
                found_contact = contact

        return found_contact

    def delete_contact(self, contact):

        self.contact_list.remove(contact)

    def edit_contact(self, edit_contact):

        found_contact = self.get_contact_by_id(edit_contact.id)

        if found_contact:
            self.delete_contact(found_contact)

            self.add_contact(edit_contact)

    def validate_phone(self, phone_number):

        try:
            parsed_phone_number = phonenumbers.parse(phone_number)
            if phonenumbers.is_possible_number(parsed_phone_number):
                return True, "Valid Phone Number"
            else:
                return False, "Please enter valid phone number"
        except Exception as e:
                return False, f"Error: {e}"


    def validate_email(self, email_address):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

        if (re.fullmatch(regex, email_address)):
            return True
        else:
            return False
