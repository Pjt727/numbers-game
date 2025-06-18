from typing import Counter
import math
import signal
from py_expression_eval import Parser
import random
import sys


NUMS = "0123456789"
OPERATORS = "-+*%!"
parser = Parser()


# have a nice C-c handler
def signal_handler(*_):
    print(" Exiting...")
    return sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


def generate_start_inventory() -> Counter:
    starting_nums = "".join(random.choices(NUMS, k=6))
    starting_operators = "".join(random.choices(OPERATORS, k=5))
    return Counter(starting_nums + starting_operators)


def random_items_after_round() -> Counter:
    starting_nums = "".join(random.choices(NUMS, k=3))
    starting_operators = "".join(random.choices(OPERATORS, k=2))
    return Counter(starting_nums + starting_operators)


class Game:
    def __init__(self) -> None:
        self.parser: Parser = Parser()
        self.inventory: Counter = generate_start_inventory()
        self.score = 0
        self.turn = 0
        self.running = True

    def game_loop(self):
        while self.running:
            self.play_round()
            if self.turn % 3 == 0:
                self.inventory += random_items_after_round()

        user_input = input("Enter r to replay the game: ")
        if user_input.lower() == "r":
            self.running = True
            self.inventory = generate_start_inventory()
            self.game_loop()

    def play_round(self):
        print(f"Inventory:\n{self.inventory_pretty()}")
        current_target = self.get_target()
        print(f"Target 🎯: {current_target}")
        # reask user until they make an expression alotted in their inventory
        user_expression = input()
        while (len(user_expression) == 0) or not self.take_from_inventory(
            user_expression
        ):
            print(
                "Invalid response. You do not have enough symbols for that! Try again!"
            )
            user_expression = input()
        user_result = self.evaluate_expression(user_expression)
        if user_result == current_target:
            print("Correct ✅")
            # TODO: score may change dpeending on something
            self.score += 1
            self.turn += 1
            user_value = input("Press anything (except q) to continue or q to quit: ")
            if user_value.lower() == "q":
                self.running = False
                print(f"You Quit 🫵 Score: {self.score} 😥")
            else:
                print("\033[2J\033[H")  # ]]clears screen
        else:
            print(f"{user_result} is Wrong❗ You Lose 🫵 Score: {self.score} 😅")
            self.running = False

    def get_target(self) -> int:
        return random.randint(-20, 20)
        # return 1

    def inventory_pretty(self) -> str:
        # TODO: add colors to symbols
        return "\n".join(
            f"'{symbol}' - {count}"
            for symbol, count in sorted(self.inventory.items(), key=lambda i: i[0])
        )

    def take_from_inventory(self, user_expression) -> bool:
        """returns true if valid false if cannot be taken, does actually take if it is valid"""
        user_counter = Counter(user_expression)
        is_valid = all(
            char in self.inventory and self.inventory[char] >= count
            for char, count in user_counter.items()
        )
        if is_valid:
            self.inventory = self.inventory - Counter(user_expression)
            return True
        return False

    # documentation on evaluate
    # https://pypi.org/project/py-expression-eval/
    def evaluate_expression(self, expression: str) -> float:
        # preprocess string for fact
        running_number: str = ""
        expression_copy = expression
        for symbol in expression_copy:
            if symbol in OPERATORS:
                if symbol == "!":
                    fact_result = math.factorial(int(running_number))
                    expression = expression.replace(
                        running_number + "!", str(fact_result)
                    )

                running_number = ""
            else:
                running_number += symbol

        return self.parser.parse(expression).evaluate({})


def main():
    game = Game()
    game.game_loop()


if __name__ == "__main__":
    main()
