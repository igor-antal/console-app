from customer import Customer


class Database:
    """
    Database storing instances of Customer class in cache memory.

    Attributes
    ----------
    __database : list_
        List holding Customer type objects.
    """
    def __init__(self):
        self.__database = []

    @property  # __database getter
    def database(self) -> list:
        return self.__database

    def __len__(self) -> int:
        """
        Counts number of Customer instances in __database attribute.

        Returns
        -------
        integer
            Length of __database list.
        """
        return len(self.database)

