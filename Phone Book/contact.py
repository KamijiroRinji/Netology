class Contact:
    """Class for creating contacts.

    Attributes
    __________
        name : str, required
            The contact's name or first name or given name
        surname : str, required
            The contact's surname or second name or family name
        phone_number : str, required
            The contact's phone number
        favorite_number : bool, optional
            The contact's status - True for favorite numbers (default False)

        Keyword Arguments:
            The contact's additional information, e.g.
            more phone numbers (second_number='+636474822'),
            email (email='jhony@smith.com'),
            SNS (telegram='@jhony') etc

    Methods
    _______
    dict_printer(contact_dict)
        Helps to print additional information beautifully
    """
    def __init__(self, name, surname, phone_number, fav_number=False, **kwargs):
        """
        Arguments
        __________
            name : str, required
                The contact's name or first name or given name
            surname : str, required
                The contact's surname or second name or family name
            phone_number : str, required
                The contact's phone number
            favorite_number : bool, optional
                The contact's status - True for favorite numbers (default False)

            Keyword Arguments:
                The contact's additional information, e.g.
                more phone numbers (second_number='+636474822'),
                email (email='jhony@smith.com'),
                SNS (telegram='@jhony') etc
        """
        self.contact_name = name
        self.surname = surname
        self.phone_number = phone_number
        self.favorite_number = fav_number
        self.contact_dict = kwargs

    def dict_printer(self, contact_dict):
        """Helps to print additional information beautifully.

        Parameters
        __________
            contact_dict : dict, required
                The contact's additional information from keyword arguments
        """
        dict_lines = ''
        for key, value in contact_dict.items():
            dict_lines += f'\t{key} : {value}\n'
        return dict_lines

    def __str__(self):
        required_data = f'Имя: {self.contact_name}\nФамилия: {self.surname}\nТелефон: {self.phone_number}\n'
        if self.favorite_number:
            optional_data = 'В избранных: Да\n'
        else:
            optional_data = 'В избранных: Нет\n'
        if self.contact_dict:
            extra_data = f'Дополнительная информация:\n{self.dict_printer(self.contact_dict)}'
            return required_data + optional_data + extra_data
        else:
            return required_data + optional_data
