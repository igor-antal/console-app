from typing import Type


class Customer:
    """
    Class holding customer information and formatting it for easy reading.

    Attributes
    ----------
    __name : string
        Customers name.
    __surname : string
        Customers surname.
    __age : integer
        Customers age.
    __phone_number : string
        Customers phone number.
    """

    def __init__(self, name: str, surname: str, age: int, phone_number: str):
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__phone_number = phone_number

    @property  # __name getter
    def name(self) -> str:
        return self.__name

    @property  # __surname getter
    def surname(self) -> str:
        return self.__surname

    def __str__(self) -> str:
        """
        Formats class attributes for easy reading.

        Returns
        -------
        string
        """
        return "Jméno: {0} {1} / Věk: {2} let / Telefonní Číslo: {3}\n".format(self.name.capitalize(),
                                                                               self.surname.capitalize(),
                                                                               self.__age, self.__phone_number)
