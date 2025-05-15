# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from data.Database import Database


class GameCategory:
    __name = ""
    __description = ""
    __genre = ""
    __map = {}

    def __init__(self, name, description, genre):
        self.__name = name
        self.__description = description
        self.__genre = genre
        self.__class__.__map[self.get_key()] = self

    def get_key(self):
        return f"{self.__name}: {self.__genre}".lower()

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def __str__(self):
        return f"<{self.__name} is a {self.__description}: {self.__genre}>"

    @staticmethod
    def get_games():
        return Database.get_games()
