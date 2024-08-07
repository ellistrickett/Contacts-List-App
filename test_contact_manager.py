import unittest
from unittest import mock

from contact import Contact
from contact_manager import ContactManager


class TestContactManager(unittest.TestCase):

    test_contact_object_darwin = Contact(
        "a1ffb27c-f1d1-4e60-bf82-0f94f7434e91",
        "Darwin",
        "Nunez",
        "+447519371555",
        "darwin@darwin.com",
        "2024-05-16 19:19:11.077222",
    )

    test_contact_object_mo = Contact(
        "1fcd6501-6f43-4bcc-b579-1b8785cc3683",
        "Mo",
        "Salah",
        "+12332322774",
        "mo@mo.com",
        "2024-05-16 19:19:11.077222",
    )

    test_contact_darwin = {
        "id": "a1ffb27c-f1d1-4e60-bf82-0f94f7434e91",
        "first_name": "Darwin",
        "last_name": "Nunez",
        "phone_number": "+447519371555",
        "email_address": "darwin@darwin.com",
        "date_time_updated": "2024-05-16 19:19:11.077222",
    }

    test_contact_mo = {
        "id": "1fcd6501-6f43-4bcc-b579-1b8785cc3683",
        "first_name": "Mo",
        "last_name": "Salah",
        "phone_number": "+12332322774",
        "email_address": "mo@mo.com",
        "date_time_updated": "2024-05-16 19:19:11.077222",
    }

    @mock.patch("contact_manager.json.load")
    def test_initialise_contact_list(self, mock_json_load):
        mock_json_load.return_value = [self.test_contact_darwin, self.test_contact_mo]
        contact_manager = ContactManager()
        contact_manager.initialise_contact_list()

        self.assertEqual(len(contact_manager.contact_list), 2, "Length")

        self.assertEqual(
            contact_manager.contact_list[0].id,
            "a1ffb27c-f1d1-4e60-bf82-0f94f7434e91",
            "Darwin Id",
        )

        self.assertEqual(
            contact_manager.contact_list[1].id,
            "1fcd6501-6f43-4bcc-b579-1b8785cc3683",
            "Mo Id",
        )

    @mock.patch("contact_manager.open")
    def test_write_contact_list_to_file(self, mock_open):
        contact_manager = ContactManager()
        contact_manager.write_contact_list_to_file()

        self.assertTrue(mock_open.called)
        arguments = {"file": "contact_list.json", "mode": "w"}
        mock_open.asset_called_with(arguments)

    @mock.patch("contact_manager.print")
    def test_add_contact(self, mock_print):
        contact_manager = ContactManager()
        contact_manager.add_contact(self.test_contact_darwin)

        argument = "Cannot add contact to contact list as not a Contact Object"

        self.assertEqual(len(contact_manager.contact_list), 0)
        mock_print.asset_called_with(argument)

        contact_manager.add_contact(self.test_contact_object_darwin)

        self.assertEqual(len(contact_manager.contact_list), 1)
        self.assertEqual(
            contact_manager.contact_list[0].id, "a1ffb27c-f1d1-4e60-bf82-0f94f7434e91"
        )

    def test_get_contacts(self):

        contact_manager = ContactManager()

        self.assertEqual(contact_manager.get_contacts(), [])
        contact_manager.get_contacts()

    def test_get_contact_by_id(self):

        contact_manager = ContactManager()
        contact_manager.contact_list = [
            self.test_contact_object_darwin,
            self.test_contact_object_mo,
        ]

        self.assertEqual(
            contact_manager.get_contact_by_id("a1ffb27c-f1d1-4e60-bf82-0f94f7434e91"),
            self.test_contact_object_darwin,
        )

        contact_manager.contact_list = [self.test_contact_object_mo]

        self.assertEqual(
            contact_manager.get_contact_by_id("a1ffb27c-f1d1-4e60-bf82-0f94f7434e91"),
            None,
        )

    def test_search_contact(self):
        contact_manager = ContactManager()
        contact_manager.contact_list = [
            self.test_contact_object_darwin,
            self.test_contact_object_mo,
        ]

        self.assertEqual(
            contact_manager.search_contact("Darwin"),
            self.test_contact_object_darwin,
        )

        self.assertEqual(
            contact_manager.search_contact("Salah"),
            self.test_contact_object_mo,
        )

        self.assertEqual(
            contact_manager.search_contact("+12332322774"),
            self.test_contact_object_mo,
        )

        self.assertEqual(
            contact_manager.search_contact("mo@mo.com"),
            self.test_contact_object_mo,
        )

    def test_delete_contact(self):
        contact_manager = ContactManager()
        contact_manager.contact_list = [
            self.test_contact_object_darwin,
            self.test_contact_object_mo,
        ]

        contact_manager.delete_contact(self.test_contact_object_mo)

        self.assertEqual(
            len(contact_manager.contact_list),
            1,
        )

        self.assertEqual(
            contact_manager.contact_list[0],
            self.test_contact_object_darwin,
        )

    def test_edit_contact(self):
        contact_manager = ContactManager()
        contact_manager.contact_list = [
            self.test_contact_object_darwin,
            self.test_contact_object_mo,
        ]

        test_edit_contact_object_darwin = Contact(
            "a1ffb27c-f1d1-4e60-bf82-0f94f7434e91",
            "Darwin",
            "Nunez",
            "+447586545975",
            "darwin@darwin.com",
            "2024-05-16 19:19:11.077222",
        )

        contact_manager.edit_contact(test_edit_contact_object_darwin)

        self.assertEqual(contact_manager.contact_list[1].phone_number, "+447586545975")
