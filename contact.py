# contact.py - Contact Module
# Responsible for creating a contact record

# You may add extra fields to the contact record


# Class responsible for Contact and ca be called to create one providing the required instance attributes
class Contact:
    def __init__(
        self, id, first_name, last_name, phone_number, email_address, date_time_updated
    ):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email_address = email_address
        self.date_time_updated = date_time_updated
