from logic.GameCategory import GameCategory


class PlayedGames(GameCategory):
    __hours_played = 0
    __rating = 0

    def __init__(self, name, description, genre, hours_played, rating):
        super().__init__(name, description, genre)
        self.__hours_played = hours_played
        self.__rating = rating

    def get_key(self):
        f"{self.get_name()}: {self.get_description()} at {self.__hours_played} on {self.__rating}".lower()
