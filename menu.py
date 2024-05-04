# menu.py - Menu Module
# Responsible for displaying and implementing the menu options

from tkinter import *
from tkinter.ttk import Treeview
from PIL import ImageTk, Image
import uuid

from contact_manager import get_contacts, add_contact, search_contact, delete_contact, edit_contact, get_contact_by_id

from contact import create_contact, validate_email, validate_phone

class Menu():
    def __init__(self, master):
        self.master = master
        self.master.title("MENU")

        self.checked_image = ImageTk.PhotoImage(Image.open("approved.png").resize((10, 10)))
        self.unchecked_image = ImageTk.PhotoImage(Image.open("unchecked.png").resize((10, 10)))

        Button(self.master, text="Display Contacts", command = self.display_contacts).grid(row=1, column=0)
        Button(self.master, text="Edit Contact", command = self.edit_popup).grid(row=1, column=1)
        Button(self.master, text="Add Contact", command = self.add_popup).grid(row=1, column=2)
        Button(self.master, text="Delete Contact", command = self.delete_contacts).grid(row=1, column=3)
        Button(self.master, text="Quit", command = self.master.destroy).grid(row=1, column=4)

        self.tree = Treeview(self.master, column=(1, 2, 3, 4, 5), height=5)

        self.tree.tag_configure("checked", image = self.checked_image)
        self.tree.tag_configure("unchecked", image = self.unchecked_image)

        self.tree.column(1, anchor=CENTER)
        self.tree.heading(1, text="")

        self.tree.bind("<Button 1>", self.select_row)

        self.tree.column(2, anchor=CENTER)
        self.tree.heading(2, text="First Name")
        self.tree.column(3, anchor=CENTER)
        self.tree.heading(3, text="Last Name")
        self.tree.column(4, anchor=CENTER)
        self.tree.heading(4, text="Phone Number")
        self.tree.column(5, anchor=CENTER)
        self.tree.heading(5, text="Email Address")

        self.tree.grid(row = 2, columnspan = 5)

        self.entry_search_bar = Entry(self.master)
        self.entry_search_bar.grid(row = 8, column = 0)

        Button(self.master, text="Search Contact", command = self.search_contact).grid(row=8, column=1)

        self.label_search_bar_notify = Label(self.master)
        self.label_search_bar_notify.grid(row = 8, column = 2)

    def search_contact(self):

        contact = search_contact(self.entry_search_bar.get())

        if contact:
            self.label_search_bar_notify.config(text = "")
            self.remove_tree_contacts()

            self.tree.insert('', 'end', text=1, values=(contact["id"], contact["first_name"], contact["last_name"], contact["phone_number"], contact["email_address"]), tags = ("unchecked"))
        else:
            self.label_search_bar_notify.config(text = "No Contact Found", fg = "red")
        
    def remove_tree_contacts(self):

        for contact in self.tree.get_children():
            self.tree.delete(contact)

    def display_contacts(self):

        self.remove_tree_contacts()

        contacts_list = get_contacts()

        for index, contact in enumerate(contacts_list, start=1): 
            self.tree.insert('', 'end', text=index, values=(contact["id"], contact["first_name"], contact["last_name"], contact["phone_number"], contact["email_address"]), tags = ("unchecked"))

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

    def get_checked_tree_contacts(self):
        checked_contacts = []

        for contact in self.tree.get_children():
            tag = self.tree.item(contact, "tags")[0]
            if tag == "checked":
                checked_contacts.append(contact)

        return checked_contacts

    def delete_contacts(self):

        checked_contacts = self.get_checked_tree_contacts()

        if len(checked_contacts) == 0:
            return self.open_popup_warning("delete")

        for contact in checked_contacts:
            self.tree.delete(contact)
            contact_id = list(self.tree.item(contact).values())[2][0]
            delete_contact(get_contact_by_id(contact_id))

    def open_popup(self, isEdit):
        if isEdit:
            checked_contacts = self.get_checked_tree_contacts()

            if len(checked_contacts) > 1:
                return self.open_popup_warning("multiple")
            elif len(checked_contacts) == 0:
                return self.open_popup_warning("edit")

            contact_id = list(self.tree.item(checked_contacts[0]).values())[2][0]
            self.contact_for_popup = get_contact_by_id(contact_id)

        self.contact_pop_up= Toplevel(self.master)
        self.contact_pop_up.geometry("600x150")
        self.contact_pop_up.title("Contact Window")

        if isEdit:
            self.label_id = Label(self.contact_pop_up, text = f'Id: {self.contact_for_popup["id"]}')
            self.label_id.grid(row = 3, column = 0)

        self.label_first_name = Label(self.contact_pop_up, text="First Name:")
        self.label_first_name.grid(row = 4, column = 0)

        first_name = StringVar()

        self.entry_first_name = Entry(self.contact_pop_up, textvariable = first_name)
        self.entry_first_name.grid(row = 4, column = 1)

        self.label_last_name = Label(self.contact_pop_up, text="Last Name:")
        self.label_last_name.grid(row = 5, column = 0)

        last_name = StringVar()

        self.entry_last_name = Entry(self.contact_pop_up, textvariable = last_name)
        self.entry_last_name.grid(row = 5, column = 1)

        self.label_phone_number = Label(self.contact_pop_up, text="Phone Number:")
        self.label_phone_number.grid(row = 6, column = 0)

        phone_number = StringVar()

        self.entry_phone_number = Entry(self.contact_pop_up, textvariable = phone_number)
        self.entry_phone_number.grid(row = 6, column = 1)

        self.label_phone_number_notify = Label(self.contact_pop_up)
        self.label_phone_number_notify.grid(row = 6, column = 2)

        self.label_email_address = Label(self.contact_pop_up, text="Email Address:")
        self.label_email_address.grid(row = 7, column = 0)

        email_address = StringVar()

        self.entry_email_address = Entry(self.contact_pop_up, textvariable = email_address)
        self.entry_email_address.grid(row = 7, column = 1)

        self.label_email_addrees_notify = Label(self.contact_pop_up)
        self.label_email_addrees_notify.grid(row = 7, column = 2)

        if isEdit:
            self.entry_first_name.insert(0, self.contact_for_popup["first_name"])
            self.entry_last_name.insert(0, self.contact_for_popup["last_name"])
            self.entry_phone_number.insert(0, self.contact_for_popup["phone_number"])
            self.entry_email_address.insert(0, self.contact_for_popup["email_address"])
            self.edit_contact_button = Button(self.contact_pop_up, text="Edit Contact", command = self.edit_contact).grid(row=8, column=1)
        else:
            self.add_contact_button = Button(self.contact_pop_up, text="Add Contact", command = self.add_contact).grid(row=8, column=1)

    def edit_popup(self):
        self.open_popup(True)

    def add_popup(self):
        self.open_popup(False)

    def add_contact(self):
        is_valid_contact = self.validate_contact_input()

        if is_valid_contact:
            contact = create_contact(uuid.uuid4(), self.entry_first_name.get(), self.entry_last_name.get(), self.entry_phone_number.get(), self.entry_email_address.get())
            add_contact(contact)
            self.close_popup()

    def edit_contact(self):
        
        is_valid_contact = self.validate_contact_input()

        if is_valid_contact:
            contact = create_contact(self.contact_for_popup["id"], self.entry_first_name.get(), self.entry_last_name.get(), self.entry_phone_number.get(), self.entry_email_address.get())
            edit_contact(contact)
            self.close_popup()

    def close_popup(self):
        self.contact_pop_up.destroy()
        self.contact_pop_up.update()
        self.display_contacts()

    def open_popup_warning(self, popUpType):

        warning_title = ""
        warning_text = ""

        if popUpType == "delete":
            warning_title = "No Contact Selected"
            warning_text = "Warning: You must select one contact to delete contact"
        elif popUpType == "edit":
            warning_title = "No Contact Selected"
            warning_text = "Warning: You must select one contact to edit contact"
        elif popUpType == "multiple":
            warning_title = "Edit Multiple Popup Warning"
            warning_text = "Warning: You cannot edit multiple contcts at once. Please check one box at a time"

        self.popup_warning = Toplevel(self.master)
        self.popup_warning.geometry("600x150")
        self.popup_warning.title(warning_title)

        frame = Frame(self.popup_warning)
        frame.place(relx=0.5, rely=0.5, anchor="c")

        self.popup_warning_label = Label(frame, text=warning_text, fg='red')
        self.popup_warning_label.grid(row=0, column=0, columnspan=2)

        self.close_pop_up_button = Button(frame, text="Ok", command = self.popup_warning.destroy)
        self.close_pop_up_button.grid(row=1, column=0, columnspan=2)

    def validate_contact_input(self):
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
           return True

