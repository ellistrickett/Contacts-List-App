# menu.py - Menu Module
# Responsible for displaying and implementing the menu options

from tkinter import *
from tkinter.ttk import Treeview
import re
import phonenumbers
from PIL import ImageTk, Image

from contact_manager import get_contacts, add_contact, search_contact, delete_contact

from contact import create_contact, validate_email, validate_phone

class Menu():
    def __init__(self, master):
        self.master = master
        self.master.title("MENU")

        self.checked_image = ImageTk.PhotoImage(Image.open("approved.png").resize((10, 10)))
        self.unchecked_image = ImageTk.PhotoImage(Image.open("unchecked.png").resize((10, 10)))

        self.button1 = Button(self.master, text="Display Contacts", command = self.display_contacts).grid(row=1, column=0)
        self.button4 = Button(self.master, text="Delete Contact", command = self.delete_contacts).grid(row=1, column=3)
        self.button5 = Button(self.master, text="Quit").grid(row=1, column=4)

        self.tree = Treeview(self.master, column=(1, 2, 3, 4), height=5)

        self.tree.tag_configure("checked", image = self.checked_image)
        self.tree.tag_configure("unchecked", image = self.unchecked_image)

        self.tree.column("# 0", anchor=CENTER)
        self.tree.heading("# 0", text="")

        self.tree.bind("<Button 1>", self.select_row)

        self.tree.column(1, anchor=CENTER)
        self.tree.heading(1, text="First Name")
        self.tree.column(2, anchor=CENTER)
        self.tree.heading(2, text="Last Name")
        self.tree.column(2, anchor=CENTER)
        self.tree.heading(3, text="Phone Number")
        self.tree.column(4, anchor=CENTER)
        self.tree.heading(4, text="Email Address")

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

        self.add_contact_button = Button(self.master, text="Add Contact", command = self.add_contact).grid(row=7, column=1)

        self.entry_search_bar = Entry(self.master)
        self.entry_search_bar.grid(row = 8, column = 0)

        self.button_search_bar = Button(self.master, text="Search Contact", command = self.search_contact).grid(row=8, column=1)

        self.label_search_bar_notify = Label(self.master)
        self.label_search_bar_notify.grid(row = 8, column = 2)

    def search_contact(self):

        contact = search_contact(self.entry_search_bar.get())

        if contact:
            self.remove_tree_contacts()

            self.tree.insert('', 'end', text=1, values=(contact["first_name"], contact["last_name"], contact["phone_number"], contact["email_address"]), image = "unchecked")
        else:
            self.label_search_bar_notify.config(text = "No Contact Found", fg = "red")
        
    def remove_tree_contacts(self):

        for contact in self.tree.get_children():
            self.tree.delete(contact)

    def display_contacts(self):

        self.remove_tree_contacts()

        contacts_list = get_contacts()

        for index, contact in enumerate(contacts_list, start=1): 
            self.tree.insert('', 'end', text=index, values=(contact["first_name"], contact["last_name"], contact["phone_number"], contact["email_address"]), tags = ("unchecked"))

    def add_contact(self):

        is_email_valid = validate_email(self.entry_email_address.get())

        if is_email_valid:
            self.label_email_addrees_notify.config(text = "Valid Email Address", fg = "green")
        else:
            self.label_email_addrees_notify.config(text = "Please enter valid email address", fg = "red")

        is_phone_valid = validate_phone(self.entry_phone_number.get())

        if is_phone_valid["is_phone_valid"]:
            self.label_phone_number_notify.config(text = is_phone_valid["message"], fg = "green")
        else:
            self.label_phone_number_notify.config(text = is_phone_valid["message"], fg = "red")

        if (is_email_valid and is_phone_valid["is_phone_valid"]):
            contact = create_contact(self.entry_first_name.get(), self.entry_last_name.get(), self.entry_phone_number.get(), self.entry_email_address.get())
            add_contact(contact)

    def select_row(self, event):
        
        row_id = self.tree.identify_row(event.y)
        tag = self.tree.item(row_id, "tags")[0]
        tags = list(self.tree.item(row_id, "tags"))
        tags.remove(tag)
        self.tree.item(row_id, tags = tags)

        if tag == "checked":
            self.tree.item(row_id, tags = "unchecked")
        else:
            self.tree.item(row_id, tags = "checked")

    def delete_contacts(self):

        for contact in self.tree.get_children():
            tag = self.tree.item(contact, "tags")[0]
            if tag == "checked":
                self.tree.delete(contact)
            





        # self.master.destroy()

