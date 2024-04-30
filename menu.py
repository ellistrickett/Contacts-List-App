# menu.py - Menu Module
# Responsible for displaying and implementing the menu options

from tkinter import *
from tkinter.ttk import Treeview

from contact_manager import get_contacts, add_contact, search_contact, delete_contact

from contact import display_contact, input_contact

class Menu():
    def __init__(self, master):
        self.master = master
        # self.master.geometry("400x400")
        self.master.title("MENU")
        # self.label = Label(self.master, text = "Welcome to Contact Manager GUI", fg="red").grid(row = 0, column = 0)

        # self.variable = StringVar()
        # self.w = StringVar()
        # self.variable.set("Click to choose your option")

        self.button1 = Button(self.master, text="Display Contacts", command = self.display_contacts).grid(row=1, column=0)
        self.button2 = Button(self.master, text="Add Contact").grid(row=1, column=1)
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
        # frame1 = Frame(self.master)
        # frame1.grid(row=2,columnspan=4, sticky=E+W)

        # self.list_box1 = Listbox(frame1, height=5, width=60)
        # self.list_box1.grid(row = 2, column = 0)

        # OptionMenu(self.master, self.variable, "1. Display Contacts", "2. Add Contact", "3. Search Contact", "4. Delete Contact", "5. Quit").grid(row=1, column=3)
        # self.button1 = Button(self.master, text="Go", command = self.cmdgo).grid(row=2, column=3)
        
    def display_contacts(self):
        # Lb1 = Listbox(self.master)
        # Lb1.grid(row=3, column=3)

        contacts_list = get_contacts()

        for index, contact in enumerate(contacts_list, start=1):
            # print("Contact", index)
            # self.list_box1.insert(0, contact["first_name"])
            # self.list_box1.insert(0, contact["last_name"])
            # self.list_box1.insert(0, contact["phone_number"])
            # self.list_box1.insert(0, contact["email_address"])          
            self.tree.insert('', 'end', text=index, values=(contact["first_name"], contact["last_name"], contact["phone_number"], contact["email_address"]))

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



