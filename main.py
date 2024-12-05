from typing import Counter
from py_expression_eval import Parser
import random

NUMS = "0123456789"
OPERATORS = "-+"
parser = Parser()


def generate_start_iventory() -> Counter:
    starting_nums = "".join(random.choices(NUMS, k=12))
    starting_operators = "".join(random.choices(OPERATORS, k=4))
    return Counter(starting_nums + starting_operators)


class Game:
    def __init__(self) -> None:
        self.parser: Parser = Parser()
        self.inventory: Counter = generate_start_iventory()

    def start_round(self):
        print(
            f"Inventory:\n{ "\n".join([f"'{symbol}', {count}" for symbol, count in self.inventory.items()]) }"
        )
        print(f"Target 🎯: {self.get_target()}")

    def get_target(self) -> int:
        return random.randint(-50, 50)

    # documentation on evaluate
    # https://pypi.org/project/py-expression-eval/
    def evaluate_expression(self, expression: str) -> float:
        return self.parser.parse(expression).evaluate({})


def main():
    game = Game()
    game.start_round()


if __name__ == "__main__":
    main()
