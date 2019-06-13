import contact


class PhoneBook:
    """Class for creating phone books.

        Attributes
        __________
            name : str, required
                The phone book's name

        Methods
        _______
            add_contact(contact)
                Add a contact to phone book

            delete_contact(contact_phone_number)
                Delete a contact from the phone book by the contact's phone number
        """
    def __init__(self, name):
        self.phonebook_name = name
        self.contacts = []
        self.contacts_phone_numbers = []
        self.contacts_names = []
        self.contacts_surnames = []

    def add_contact(self, contact):
        """Add a contact to phone book.

        Contacts' phone numbers should be unique, thus if the phone book already contains
        a contact with the same phone_number the recurrance won't be added.

        Arguments
        __________
            contact : Contact
                The Contact object to add to the phone book
        """
        if contact.phone_number in self.contacts_phone_numbers:
            print(f'Контакт с номером телефона {contact.phone_number} '
                  f'уже присутствует в телефонной книге {self.phonebook_name}, поэтому не будет добавлен.')
        else:
            self.contacts.append(contact)
            print(f'Контакт {contact.contact_name} {contact.surname} '
                  f'добавлен в телефонную книгу {self.phonebook_name}.')
            self.contacts_phone_numbers.append(contact.phone_number)
            self.contacts_names.append(contact.contact_name)
            self.contacts_surnames.append(contact.surname)

    def delete_contact(self, contact_phone_number):
        """Delete a contact from the phone book by the contact's phone number.

        If the phone book doesn't contain a contact with the provided phone number,
        nothing will be deleted.

        Arguments
        __________
            contact_phone_number : str, required
                The contact's phone number
        """
        # phone_book.delete('+999')
        if contact_phone_number in self.contacts_phone_numbers:
            for contact in self.contacts:
                if contact.phone_number == contact_phone_number:
                    self.contacts.remove(contact)
                    print(f'Контакт с номером телефона {contact.phone_number} '
                          f'удалён из телефонной книги {self.phonebook_name}.')
        else:
            print(f'Контакт с номером телефона {contact_phone_number} отсутствует в телефонной книге {self.phonebook_name}, '
                  f'поэтому не может быть удалён.')

    def find_favorite_contacts(self):
        """Finds all favorite contacts in the phone book.

        Returns
        _______
            favorite_contacts : list
                A list of favorite contacts
        """
        favorite_contacts = [contact for contact in self.contacts if contact.favorite_number]
        return favorite_contacts

    def print_favorite_contacts(self):
        """Prints all favorite contacts in the phone book."""
        favorite_contacts = self.find_favorite_contacts()
        for contact in favorite_contacts:
            print(contact)

    def find_contact_by_full_name(self, contact_name, surname):
        """Finds a contact in the phone book by the contact's full name.

        If the sought-for contact isn't found in the phone book, nothing will be returned.

        Arguments
        _________
            contact_name : str, required
                The sought-for contact's first name
            surname : str, required
                The sought-for contact's surname

        Returns
        _______
            contact : Contact
                The sought-for contact
        """
        if contact_name in self.contacts_names and surname in self.contacts_surnames:
            for contact in self.contacts:
                if contact_name == contact.contact_name and surname == contact.surname:
                    return contact
        else:
            print(
                f'Контакт с именем {contact_name} {surname} отсутствует в телефонной книге {self.phonebook_name}.')
