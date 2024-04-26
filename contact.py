# contact.py - Contact Module
# Responsible for creating a contact record

# You may add extra fields to the contact record

# Don't really need create_contact and get_full_name at this point
# def create_contact(first_name, last_name, phone_number, email_address):
#     return True
   
# def get_full_name(contact):

#     full_name = contact["first_name"] + " " + contact["last_name"]

#     return full_name
 

def display_contact(contact):

    print("First Name:", contact["first_name"]) 
    print("Last Name:", contact["last_name"])
    print("Phone Number:", contact["phone_number"])
    print("Email Address:", contact["email_address"])
  

def input_contact():
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

    return contact
   




