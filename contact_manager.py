# contact_manager.py - Contact Manager Module
# Responsible for maintaining and modifying the contact list
import json
import re

import phonenumbers

from contact import Contact


class ContactManager:
    def __init__(self):
        # When ContactManager is initialised create contact list array to hold contacts to be used in the Table
        self.contact_list = []
        self.file_name = "contact_list.json"

    # Read json file and add contacts to contact_list
    def initialise_contact_list(self):
        # Open the file with file name and set variable
        file = open(self.file_name)

        # Load the file using json external library method
        # Loop through objects and set variable as contact
        for contact in json.load(file):
            # Add contact to contact list as a Contact Object
            self.contact_list.append(
                # Create Contact object and pass instance attributes
                Contact(
                    # Get values using key
                    contact["id"],
                    contact["first_name"],
                    contact["last_name"],
                    contact["phone_number"],
                    contact["email_address"],
                    contact["date_time_updated"],
                )
            )

        # Close the file opened
        # Best practice
        file.close()

    # Wite contact_list to json
    def write_contact_list_to_file(self):

        # Open file and prepare to w (Write)
        with open(self.file_name, "w") as file:
            # Using the json library serialise the contact_list as string
            # Default vars required to serialise classes
            json.dump(self.contact_list, file, default=vars)

    # Add the contact to the contact list
    def add_contact(self, contact):
        if isinstance(contact, Contact):
            self.contact_list.append(contact)
        else:
            # Not a good way to handle this.
            # Should have validation on frontend and backend but this isnt traditional application
            print("Cannot add contact to contact list as not a Contact Object")

    # Return the contacts list
    def get_contacts(self):

        return self.contact_list

    def get_contact_by_id(self, id):

        for contact in self.contact_list:
            if contact.id == id:
                return contact

    def search_contact(self, query):

        found_contact = {}

        # Loop through all contacts in list and check if query matches any of the values
        # Could extend to find contact values like query
        for contact in self.contact_list:
            if contact.first_name == query:
                found_contact = contact
            elif contact.last_name == query:
                found_contact = contact
            elif contact.phone_number == query:
                found_contact = contact
            elif contact.email_address == query:
                found_contact = contact

        return found_contact

    def delete_contact(self, contact):

        # Find contact using the edited contacts Id
        found_contact = self.get_contact_by_id(contact.id)

        # If contact is found, delete it and the add the edited contact
        if found_contact:
            # Remove contact from contact list
            self.contact_list.remove(contact)

    def edit_contact(self, edit_contact):

        if self.delete_contact(edit_contact):
            self.add_contact(edit_contact)

    # Validate phone number using external library and return tuple
    # Including whether it was succesful or not with warning message for UI
    def validate_phone(self, phone_number):

        try:
            parsed_phone_number = phonenumbers.parse(phone_number)
            if phonenumbers.is_possible_number(parsed_phone_number):
                return True, "Valid Phone Number"
            else:
                return False, "Please enter valid phone number"
        except Exception as e:
            return False, f"Error: {e}"

    # GeeksForGeeks, 2023. "Check if email address valid or not in Python" [Online]
    # Place of publication: https://www.geeksforgeeks.org.
    # Available from: https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/
    # [Accessed 17 May 2024]
    # Validate email using regex and return true or false
    def validate_email(self, email_address):
        regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"

        return re.fullmatch(regex, email_address)
