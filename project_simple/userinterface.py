class UserInterface:
    """
    Static class managing user inputs and console rendering.

    Attributes
    ---------
    text_cache : string
        Text cache managed by other methods. Can be displayed in console.
    """

    text_cache = ""

    @staticmethod
    def get_string(custom_text, only_alpha=False) -> str:
        """
        Gets string type input from user.

        Parameters
        ----------
        custom_text : string
            Text of Input prompt in console.
        only_alpha : bool, default=False
            Defines, if user input can be only letters of alphabet.

        Returns
        -------
        u_input : string
            User input any text, OR only letters of alphabet if only_alpha is True.
        """
        only_alpha = only_alpha
        invalid = True
        while invalid:
            u_input = input("{}".format(custom_text)).strip().lower()
            if only_alpha and u_input.isalpha():
                return u_input
            if u_input and only_alpha:
                print("Zadejte pouze písmena.")
            if not only_alpha and u_input:
                return u_input

    @staticmethod
    def get_integer(custom_text) -> int:
        """
        Gets integer type input from user.

        Parameters
        ----------
        custom_text : string
            Text of Input prompt in console.

        Returns
        -------
        u_input : integer
            User input number
        """
        invalid = True
        while invalid:
            try:
                u_input = int(input("{}".format(custom_text)))
                return u_input
            except ValueError:
                print("Zadejte pouze celá čísla.")

    @staticmethod
    def render_menu():
        """
        Renders option menu in console.
        """
        print("------------------------------")
        print("Evidence pojistníků")
        print("------------------------------")
        print()
        print("Vyberte si akci")
        print("1 - Přidat nového pojistníka")
        print("2 - Vypsat všechny pojistníky")
        print("3 - Vyhledat pojistníka")
        print("4 - Konec")
        print()
        print("Vaše volba: ")

    @staticmethod
    def get_menu_choice() -> int:
        """
        Gets users choice from option menu.

        Returns
        -------
        u_input : integer
            User input number in range 1-4.
        """
        wrong_choice_message = "Zadejte číslo v rozmezí 1 až 4."
        invalid = True
        while invalid:
            try:
                u_input = int(input())
                if u_input in range(1, 5):
                    return u_input
                print(wrong_choice_message)
            except ValueError:
                print(wrong_choice_message)

    @staticmethod
    def continue_input():
        """
        Prompts user to press enter, pauses the program.
        """
        input("Pro pokračování stiskněte Enter ...")

    def print_text_cache(cls):
        """
        Displays text in text_cache class attribute.
        """
        print(cls.text_cache)
