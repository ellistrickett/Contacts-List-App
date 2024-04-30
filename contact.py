# contact.py - Contact Module
# Responsible for creating a contact record

# You may add extra fields to the contact record

# Don't really need create_contact and get_full_name at this point

import phonenumbers
import re

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

    contact["phone_number"] = get_valid_phone_number() 

    contact["email_address"] = get_valid_email_address()

    return contact

def get_valid_phone_number():
    is_number_valid = False

    while is_number_valid == False:
        phone_number = input("Phone Number: ")
        try:
            parsed_phone_number = phonenumbers.parse(phone_number)
            if phonenumbers.is_possible_number(parsed_phone_number):
                is_number_valid = True
                return phone_number
            else:
                print("Number is not valid, please try again")
        except Exception as e:
            print(f"Error: {e}")

def get_valid_email_address():
    is_email_valid = False
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    while is_email_valid == False:
        email = input("Email Address: ")

        if(re.fullmatch(regex, email)):
            is_email_valid = True
        else:
            print("Invalid Email, please try again")

        







