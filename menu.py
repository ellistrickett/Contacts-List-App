# menu.py - Menu Module
# Responsible for displaying and implementing the menu options

from tkinter import *
from tkinter.ttk import Treeview
import re
import phonenumbers

from contact_manager import get_contacts, add_contact, search_contact, delete_contact

from contact import display_contact, input_contact, create_contact

class Menu():
    def __init__(self, master):
        self.master = master
        self.master.title("MENU")

        self.button1 = Button(self.master, text="Display Contacts", command = self.display_contacts).grid(row=1, column=0)
        # self.button2 = Button(self.master, text="Add Contact").grid(row=1, column=1)
        self.button3 = Button(self.master, text="Search Contact").grid(row=1, column=2)
        self.button4 = Button(self.master, text="Delete Contact").grid(row=1, column=3)
        self.button5 = Button(self.master, text="Quit").grid(row=1, column=4)

        self.tree = Treeview(self.master, column=("c1", "c2", "c3", "c4"), show='headings', height=5)

        self.tree.column("# 1", anchor=CENTER)
        self.tree.heading("# 1", text="First Name")
        self.tree.column("# 2", anchor=CENTER)
        self.tree.heading("# 2", text="Last Name")
        self.tree.column("# 3", anchor=CENTER)
        self.tree.heading("# 3", text="Phone Number")
        self.tree.column("# 4", anchor=CENTER)
        self.tree.heading("# 4", text="Email Address")

        self.tree.grid(row = 2, columnspan = 5)

        self.label_first_name = Label(self.master, text="First Name:")
        self.label_first_name.grid(row = 3, column = 0)

        self.entry_first_name = Entry(self.master)
        self.entry_first_name.grid(row = 3, column = 1)

        self.label_last_name = Label(self.master, text="Last Name:")
        self.label_last_name.grid(row = 4, column = 0)

        self.entry_last_name = Entry(self.master)
        self.entry_last_name.grid(row = 4, column = 1)

        self.label_phone_number = Label(self.master, text="Phone Number:")
        self.label_phone_number.grid(row = 5, column = 0)

        self.entry_phone_number = Entry(self.master)
        self.entry_phone_number.grid(row = 5, column = 1)

        self.label_phone_number_notify = Label(self.master)
        self.label_phone_number_notify.grid(row = 5, column = 2)


        self.label_email_address = Label(self.master, text="Email Address:")
        self.label_email_address.grid(row = 6, column = 0)

        self.entry_email_address = Entry(self.master)
        self.entry_email_address.grid(row = 6, column = 1)

        self.label_email_addrees_notify = Label(self.master)
        self.label_email_addrees_notify.grid(row = 6, column = 2)

        self.button2 = Button(self.master, text="Add Contact", command = self.add_contact).grid(row=7, column=1)
        
    def display_contacts(self):

        contacts_list = get_contacts()

        for index, contact in enumerate(contacts_list, start=1): 
            self.tree.insert('', 'end', text=index, values=(contact["first_name"], contact["last_name"], contact["phone_number"], contact["email_address"]))

    def add_contact(self):

        is_email_valid = False
        is_phone_number_valid = False

        input_email_address = self.entry_email_address.get()
        input_phone_number = self.entry_phone_number.get()

        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

        if (re.fullmatch(regex, input_email_address)):
            self.label_email_addrees_notify.config(text = "Valid Email Address", fg = "green")
            is_email_valid = True
        else:
            self.label_email_addrees_notify.config(text = "Please enter valid email address", fg = "red")

        try:
            parsed_phone_number = phonenumbers.parse(input_phone_number)
            if phonenumbers.is_possible_number(parsed_phone_number):
                is_phone_number_valid = True
                self.label_phone_number_notify.config(text = "Valid Phone Number", fg = "green")
            else:
                self.label_phone_number_notify.config(text = "Please enter valid phone number", fg = "red")
        except Exception as e:
            self.label_phone_number_notify.config(text = f"Error: {e}", fg = "red")

        if (is_email_valid and is_phone_number_valid):
            contact = create_contact(self.entry_first_name.get(), self.entry_last_name.get(), input_phone_number, input_email_address)
            add_contact(contact)

        # self.master.destroy()

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

    contact = input_contact()
    
    add_contact(contact)

def option_3(query):

    found_contact = search_contact(query)

    if found_contact:
        print("Found Contact:")
        display_contact(found_contact)
    else:
        print("Contact not found")

def option_4(query):

    found_contact = search_contact(query)

    if found_contact:
        delete_contact(found_contact)
        print("Contact has been deleted")
    else:
        print("Unable to find contact")

def display_search_menu():

    print("How would you like to search for the contact?")

    print("1. First Name")
    print("2. Last Name")
    print("3. Phone Number")
    print("4. Email Address")



