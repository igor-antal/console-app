from userinterface import UserInterface
from customer import Customer
from database import Database
from os import system


class DatabaseManager:
    """
    Class creating and inserting Customer class instances into Database class.
    Also, responsible for reading Database class data.

    Attributes
    ----------
    __managed_database : Database class instance.
        Determines, which Database instance is managed by this instance of DatabaseManager.
    """
    def __init__(self, database: Database):
        self.__managed_database = database

    @property  # __managed_database getter
    def managed_database(self) -> Database:
        return self.__managed_database

    def add_new_customer(self) -> str:
        """
        Prompts user to input parameters needed for creating Customer instance using UserInterface methods.
        Then creates new Customer instance and adds it into managed database => __database list in Database instance.

        Returns
        -------
        string
            Message saying that new Customer has been successfully added.
        """
        self.managed_database.database.append(Customer(
                            UserInterface.get_string("Zadejte jméno nového pojistníka:\n", True),
                            UserInterface.get_string("Zadejte příjmení nového pojistníka:\n", True),
                            UserInterface.get_integer("Zadejte věk nového pojistníka:\n"),
                            UserInterface.get_string("Zadejte telefonní číslo nového pojistníka:\n")
                            ))
        return "Nový pojistník úspěšně přidán."

    def find_customer(self) -> str:
        """
        Searches fo Customers in (managed)Database, which values match user input.
        Prompts user to input name and surname which are then compared to __name and __surname Customer attributes.
        Mathing Customers have their values formatted into message prepared for display.

        Returns
        -------
        string
            Message informing user that database is empty. (If its empty).
        OR
        string
            Message saying that no match has been found. (If no match has been found).
        OR
        text_cache : string
            Collection of __str__ methods of Customer instances that match user input.
        """
        if len(self.managed_database) == 0:
            return "Databáze je prázdná."
        searched_name = UserInterface.get_string(
            "Zadejte jméno hledaného pojistníka:\n", True)
        searched_surname = UserInterface.get_string(
            "Zadejte příjmení hledaného pojistníka:\n", True)
        text_cache = ""
        for obj in self.managed_database.database:
            if searched_name == obj.name and searched_surname == obj.surname:
                text_cache += Customer.__str__(obj)
        if len(text_cache) == 0:
            return "Hledané jméno nenalezeno."
        return f"Nalezené shody:\n{text_cache}"

    def __str__(self) -> str:
        """
        Prepares message for display, containing attributes of all Customer instances in managed_database if there
        are any.

        Returns
        -------
        string
             Message informing user that database is empty. (If its empty).
        OR
        text_cache : string
             Collection of all __str__ methods from Customer instances, that are present in managed_database.
        """
        if len(self.managed_database) == 0:
            return "Databáze je prázdná."
        text_cache = ""
        for obj in self.managed_database.database:
            text_cache += Customer.__str__(obj)
        return text_cache

    def choice_menu(self):
        """
        Initiates choice menu. Calls on methods handling menu rendering and user input.
        Executes methods based on users choice.
        Fills text_cache in UserInterface with string outputted by other methods, so that it's ready for printing.
        """
        UserInterface.render_menu()
        u_choice = UserInterface.get_menu_choice()
        match u_choice:
            case 1:
                UserInterface.text_cache = self.add_new_customer()
                self.repeater()
            case 2:
                UserInterface.text_cache = self
                self.repeater()
            case 3:
                UserInterface.text_cache = self.find_customer()
                self.repeater()

    def repeater(self):
        """
        Initiated, after method executed by choice_menu() is finished.
        Prints text_cache that was filled by latest executed method. Then pauses the program and waits for user input.
        After that it initiates choice_menu() again.
        """
        UserInterface.print_text_cache(UserInterface)
        UserInterface.continue_input()
        system("cls")
        self.choice_menu()
