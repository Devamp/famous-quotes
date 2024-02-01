class Model:
    def select(self):
        """
        Gets all rows from the database as a list of lists.
        Row consists of quote, author, date, srcType, src, and rating.
        :return: Tuple containing all rows of database
        """
        pass

    def insert(self, quote, author, date, srcType, src, rating):
        """
        Inserts entry into database
        :param quote: String
        :param author: String
        :param date: datetime
        :param srcType: String
        :param src: String
        :param rating int
        :return: none
        :raises: Database errors on connection and insertion
        """
        pass
