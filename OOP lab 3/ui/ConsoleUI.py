from logic.GameCategory import GameCategory

from ui.input_validation import select_item


class ConsoleUI:
    CHOICES = ["l", "x"]

    @classmethod
    def init(cls):
        cls.__all_games = GameCategory.get_games()

    @classmethod
    def list_games(cls):

        @staticmethod
        def print_menu():
            print("Please select an option from the list below:")
            print("        l: List all videos")
            print("        x: Exit")

    @classmethod
    def run(cls):
        while True:
            cls.print_menu()
            choice = select_item("Please select an item: ", "Item must be a choice in the menu. ", cls.CHOICES)
            print()
            if choice == "x":
                break
            elif choice == "l":
                cls.list_games()
                print()
            print("Goodbye")


if __name__ == "__main__":
    ConsoleUI.init()
    ConsoleUI.run()
    ConsoleUI.print_menu()
