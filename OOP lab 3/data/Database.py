from logic.GameCategory import GameCategory
from logic.PlayedGames import PlayedGames

class Database:
    @staticmethod
    def get_games():
        rd2_bbl = GameCategory(
            name="Red Dead Redemption",
            description="Red Dead Redemption 2 is an open-world, action-adventure game set in 1899 America, where the Wild West is fading and lawmen are hunting down the last outlaw gangs",
            genre="Western"
        )
        cybp_bbl = GameCategory(
            name="CyberPunk 2077",
            description="Cyberpunk 2077 is an open-world, action-adventure role-playing game set in Night City, a sprawling metropolis obsessed with power, glamour, and body modification.",
            genre="Action-Adventure RPG"
        )
        rivals_btn = PlayedGames(
            name="Marval Rivals",
            description="Marvel Rivals is a Super Hero Team-based PVP Shooter in the Marvel Universe developed by Marvel Games & NetEase Games",
            genre="Team-Based PVP Shooter",
            hours_played=198,
             rating=5
        )
        dogs_btn = GameCategory(
            name="WatchDogs",
            description="This is third-person shooter/action game in which players assume the role of Aiden Pearce, a hacker trying to find an evil mastermind.",
            genre="Action"
        )


if __name__ == "__main__":
    games = Database.get_games()
    for game in games:
        print(game.get_key(), ": ", game, sep="")