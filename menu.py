# menu.py - Menu Module
# Responsible for displaying and implementing the menu options

# Import external libraries
import uuid
from tkinter import *
from tkinter.ttk import Treeview

from PIL import Image, ImageTk

# Import Contact class from other file
from contact import Contact


class Menu:
    def __init__(self, master, contact_manager):
        self.master = master
        # Set title of window
        self.master.title("MENU")

        # Create reference for ContactManager object create in contacts_main
        self.contact_manager = contact_manager

        # Open checkbox images and create a reference
        self.checked_image = ImageTk.PhotoImage(
            Image.open("approved.png").resize((10, 10))
        )
        self.unchecked_image = ImageTk.PhotoImage(
            Image.open("unchecked.png").resize((10, 10))
        )

        # Create buttons responsible for running the main functionality of the app
        # Bind buttons to method responsible
        # Grid places these in the top row of the window equally spaced out in 4 columns
        Button(
            self.master, text="Display Contacts", command=self.display_contacts
        ).grid(row=1, column=0)
        Button(self.master, text="Edit Contact", command=self.edit_popup).grid(
            row=1, column=1
        )
        Button(self.master, text="Add Contact", command=self.add_popup).grid(
            row=1, column=2
        )
        Button(self.master, text="Delete Contact", command=self.delete_contacts).grid(
            row=1, column=3
        )
        Button(self.master, text="Quit", command=self.master.destroy).grid(
            row=1, column=4
        )

        # Initiate a treeview to display contacts in a table
        self.tree = Treeview(self.master, column=(1, 2, 3, 4, 5), height=5)

        # Configure 2 tags for checked and unchecked with the appropiate image
        self.tree.tag_configure("checked", image=self.checked_image)
        self.tree.tag_configure("unchecked", image=self.unchecked_image)

        # Set Coulmns of table with headers position centre
        self.tree.column(1, anchor=CENTER)
        self.tree.heading(1, text="")

        # Bind select_row function to call when row selected
        self.tree.bind("<Button 1>", self.select_row)

        self.tree.column(2, anchor=CENTER)
        self.tree.heading(2, text="First Name")
        self.tree.column(3, anchor=CENTER)
        self.tree.heading(3, text="Last Name")
        self.tree.column(4, anchor=CENTER)
        self.tree.heading(4, text="Phone Number")
        self.tree.column(5, anchor=CENTER)
        self.tree.heading(5, text="Email Address")

        # Position the table
        self.tree.grid(row=2, columnspan=5)

        # Create the Search Bar
        self.entry_search_bar = Entry(self.master)
        # Position Search Bar
        self.entry_search_bar.grid(row=8, column=0)

        # Create the Search Bar button and bind to the search_contact function
        Button(self.master, text="Search Contact", command=self.search_contact).grid(
            row=8, column=1
        )

        # Create Label that notifies user if no contact found
        self.label_search_bar_notify = Label(self.master)
        self.label_search_bar_notify.grid(row=8, column=2)

    # Method responsible for search_contact
    def search_contact(self):

        # Call ContactManager search contact method with what is in the search bar to try rtrieve contact
        contact = self.contact_manager.search_contact(self.entry_search_bar.get())

        # If the contact is found remove what is in the table and display the found contact
        if contact:
            self.label_search_bar_notify.config(text="")
            self.remove_tree_contacts()

            self.tree.insert(
                "",
                "end",
                text=1,
                values=(
                    contact.id,
                    contact.first_name,
                    contact.last_name,
                    contact.phone_number,
                    contact.email_address,
                ),
                tags=("unchecked"),
            )
        # If the contact is not found display message to user
        else:
            self.label_search_bar_notify.config(text="No Contact Found", fg="red")

    # Remove what is in the table
    def remove_tree_contacts(self):

        for contact in self.tree.get_children():
            self.tree.delete(contact)

    # Get contacts from ContactManager and display to user
    def display_contacts(self):

        self.remove_tree_contacts()

        contacts_list = self.contact_manager.get_contacts()

        for index, contact in enumerate(contacts_list, start=1):
            self.tree.insert(
                "",
                "end",
                text=index,
                values=(
                    contact.id,
                    contact.first_name,
                    contact.last_name,
                    contact.phone_number,
                    contact.email_address,
                ),
                tags=("unchecked"),
            )

    # Logic responsible for selecting row
    def select_row(self, event):

        # Use the event passed by bind to id row
        row_id = self.tree.identify_row(event.y)
        # Get the tag associated with row
        tag = self.tree.item(row_id, "tags")[0]

        # If tag is checked then uncheck tag
        if tag == "checked":
            self.tree.item(row_id, tags="unchecked")
        # If tag is unchecked then check tag
        else:
            self.tree.item(row_id, tags="checked")

        # This in turn displays appropiate image

    # Get all rows in table with checked tag
    def get_checked_tree_contacts(self):
        # Initialise empty array rows with checked tag
        checked_contacts = []

        # Loop through all the rows in the table set variable as Contact
        for contact in self.tree.get_children():
            # Get the tage of the row
            tag = self.tree.item(contact, "tags")[0]
            # If its checked then add to the checked contacts array
            if tag == "checked":
                checked_contacts.append(contact)

        # Once loop has ended return the array so can be used
        return checked_contacts

    def delete_contacts(self):

        # Get all rows that have been selected
        checked_contacts = self.get_checked_tree_contacts()

        # If none have been selected the show warning and dont execute rest of method
        if len(checked_contacts) == 0:
            return self.open_popup_warning("delete")

        # Loop through selected rows
        for contact in checked_contacts:
            # Get the Id
            contact_id = list(self.tree.item(contact).values())[2][0]
            # Get the Contact and Delete
            self.contact_manager.delete_contact(
                self.contact_manager.get_contact_by_id(contact_id)
            )

        # Once loop has completed Display the contacts once again
        self.display_contacts()

    # Method responsible for the add and edit contact popup
    def open_popup(self, isEdit):
        # If it is an Edit contact Window make sure there is just one contact selected and get contact
        if isEdit:
            checked_contacts = self.get_checked_tree_contacts()

            # Popup warning for no row selected or mutliple
            if len(checked_contacts) > 1:
                return self.open_popup_warning("multiple")
            elif len(checked_contacts) == 0:
                return self.open_popup_warning("edit")

            # Get contact to display in popup
            contact_id = list(self.tree.item(checked_contacts[0]).values())[2][0]
            self.contact_for_popup = self.contact_manager.get_contact_by_id(contact_id)

        # Initiate popup with dimensions and title
        self.contact_pop_up = Toplevel(self.master)
        self.contact_pop_up.geometry("600x150")
        self.contact_pop_up.title("Contact Window")

        # If it is edit window then show id
        if isEdit:
            self.label_id = Label(
                self.contact_pop_up, text=f"Id: {self.contact_for_popup.id}"
            )
            self.label_id.grid(row=3, column=0)

        # Create form for user to enter contact details
        self.label_first_name = Label(self.contact_pop_up, text="First Name:")
        self.label_first_name.grid(row=4, column=0)

        first_name = StringVar()

        self.entry_first_name = Entry(self.contact_pop_up, textvariable=first_name)
        self.entry_first_name.grid(row=4, column=1)

        self.label_last_name = Label(self.contact_pop_up, text="Last Name:")
        self.label_last_name.grid(row=5, column=0)

        last_name = StringVar()

        self.entry_last_name = Entry(self.contact_pop_up, textvariable=last_name)
        self.entry_last_name.grid(row=5, column=1)

        self.label_phone_number = Label(self.contact_pop_up, text="Phone Number:")
        self.label_phone_number.grid(row=6, column=0)

        phone_number = StringVar()

        self.entry_phone_number = Entry(self.contact_pop_up, textvariable=phone_number)
        self.entry_phone_number.grid(row=6, column=1)

        self.label_phone_number_notify = Label(self.contact_pop_up)
        self.label_phone_number_notify.grid(row=6, column=2)

        self.label_email_address = Label(self.contact_pop_up, text="Email Address:")
        self.label_email_address.grid(row=7, column=0)

        email_address = StringVar()

        self.entry_email_address = Entry(
            self.contact_pop_up, textvariable=email_address
        )
        self.entry_email_address.grid(row=7, column=1)

        self.label_email_addrees_notify = Label(self.contact_pop_up)
        self.label_email_addrees_notify.grid(row=7, column=2)

        # If there is already details, display them
        # Display appropiate button
        if isEdit:
            self.entry_first_name.insert(0, self.contact_for_popup.first_name)
            self.entry_last_name.insert(0, self.contact_for_popup.last_name)
            self.entry_phone_number.insert(0, self.contact_for_popup.phone_number)
            self.entry_email_address.insert(0, self.contact_for_popup.email_address)
            self.edit_contact_button = Button(
                self.contact_pop_up, text="Edit Contact", command=self.edit_contact
            ).grid(row=8, column=1)
        else:
            self.add_contact_button = Button(
                self.contact_pop_up, text="Add Contact", command=self.add_contact
            ).grid(row=8, column=1)

    # Open Edit Contact Popup
    def edit_popup(self):
        # True shows it is pop up
        self.open_popup(True)

    # Open Add Contact Popup
    def add_popup(self):
        self.open_popup(False)

    # Add Contact Logic
    def add_contact(self):
        # Check Contact trying to add is valid and display error messages
        is_valid_contact = self.validate_contact_input()

        # If it is valid then create contact with values entered
        if is_valid_contact:
            contact = Contact(
                str(uuid.uuid4()),
                self.entry_first_name.get(),
                self.entry_last_name.get(),
                self.entry_phone_number.get(),
                self.entry_email_address.get(),
            )
            # Add contact to ContactManager list
            result = self.contact_manager.add_contact(contact)

            # Close Popup
            self.close_popup()

    # Edit Contact Logic
    def edit_contact(self):

        # Check Contact trying to add is valid and display error messages
        is_valid_contact = self.validate_contact_input()

        # If it is valid then create contact with values entered and original id
        if is_valid_contact:
            contact = Contact(
                self.contact_for_popup.id,
                self.entry_first_name.get(),
                self.entry_last_name.get(),
                self.entry_phone_number.get(),
                self.entry_email_address.get(),
            )
            # Edit Contact in ContactManager List
            self.contact_manager.edit_contact(contact)
            self.close_popup()

    # Reusable code above for edit and add contact

    # Close Popup and redisplay contacts
    def close_popup(self):
        self.contact_pop_up.destroy()
        self.contact_pop_up.update()
        self.display_contacts()

    # Probably not the best way of doing this
    # Could just pass the warning title and text
    # But display the create content for warning window needed
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

        self.popup_warning_label = Label(frame, text=warning_text, fg="red")
        self.popup_warning_label.grid(row=0, column=0, columnspan=2)

        self.close_pop_up_button = Button(
            frame, text="Ok", command=self.popup_warning.destroy
        )
        self.close_pop_up_button.grid(row=1, column=0, columnspan=2)

    # Validate contact input before adding or editing and display error to user
    def validate_contact_input(self):
        is_email_valid = self.contact_manager.validate_email(
            self.entry_email_address.get()
        )

        if is_email_valid:
            self.label_email_addrees_notify.config(
                text="Valid Email Address", fg="green"
            )
        else:
            self.label_email_addrees_notify.config(
                text="Please enter valid email address", fg="red"
            )

        is_phone_valid, message = self.contact_manager.validate_phone(
            self.entry_phone_number.get()
        )

        if is_phone_valid:
            self.label_phone_number_notify.config(text=message, fg="green")
        else:
            self.label_phone_number_notify.config(text=message, fg="red")

        if is_email_valid and is_phone_valid:
            return True
