import unittest
from unittest import mock

from contact import Contact
from contact_manager import ContactManager


class TestContactManager(unittest.TestCase):

    @mock.patch("contact_manager.json.load")
    def test_initialise_contact_list(self, mock_json_load):
        mock_json_load.return_value = [
            {
                "id": "a1ffb27c-f1d1-4e60-bf82-0f94f7434e91",
                "first_name": "Darwin",
                "last_name": "Nunez",
                "phone_number": "+447519371555",
                "email_address": "darwin@darwin.com",
            },
            {
                "id": "1fcd6501-6f43-4bcc-b579-1b8785cc3683",
                "first_name": "Mo",
                "last_name": "Salah",
                "phone_number": "+12332322774",
                "email_address": "mo@mo.com",
            },
        ]
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


# test_contact_darwin = Contact(
#     "a1ffb27c-f1d1-4e60-bf82-0f94f7434e91",
#     "Darwin",
#     "Nunez",
#     "+447519371555",
#     "darwin@darwin.com",
# )
# test_contact_mo = Contact(
#     "1fcd6501-6f43-4bcc-b579-1b8785cc3683",
#     "Mo",
#     "Salah",
#     "+12332322774",
#     "mo@mo.com",
# )
