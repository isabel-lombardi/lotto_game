
from random import sample

from lotto.bet_type import BetType
from lotto.city import City
from lotto.lotto_helper import PrintTable, PrintOutput


class Lotto:

    def __init__(self, city="", bet="", numbers=""):
        self.city = city
        self.bet = bet
        self.int_bet = 0
        self.numbers = numbers

    def choose_city(self):
        choice_mex = " Choose the 'ruota' based on the name of the city: "
        PrintOutput.header(choice_mex)
        print()

        for x, name in enumerate(City.cities, 1):
            print(" -", x, ":", name)

        PrintOutput.horizontal_line()

        while True:
            try:
                city_choice = int(input(" Enter the number corresponding to the city: "))
                PrintOutput.horizontal_line()

                if City.is_city_valid(city_choice):
                    self.city = City.city_index(city_choice)
                    break

                else:
                    print(" " * 6, "* Please enter a number between 1 to 10 * ")

            except ValueError:
                print("* Enter the number corresponding to the city, not the name * ")

    def choose_bet_type(self):
        choice_mex = " Enter the type of bet to apply for the ticket: "
        print()
        PrintOutput.header(choice_mex)

        for x, name in enumerate(BetType.bet_types, 1):
            print(" -", x, ":", name)

        PrintOutput.horizontal_line()

        while True:
            try:
                bet_choice = int(input(" Enter the number corresponding to the type of bet: "))
                PrintOutput.horizontal_line()

                if BetType.is_bet_type_valid(bet_choice):
                    self.int_bet = bet_choice
                    self.bet = BetType.bet_index(bet_choice)
                    break
                else:
                    print(" " * 6, "* Please enter a number between 1 to 5 * ")

            except ValueError:
                print("* Enter the number corresponding to the type of bet, not the name * ")

    def choose_numbers(self):
        max_numbers = 10

        print()
        choice_mex = "You can play from 1 to 10 numbers"
        PrintOutput.header(choice_mex)

        while True:
            try:
                choice_numbers = int(input(" How many numbers do you want to play?: "))
                PrintOutput.horizontal_line()

                if self.int_bet <= choice_numbers <= max_numbers:
                    self.numbers = (sorted(sample(list(range(1, 90 + 1)), choice_numbers)))
                    break
                elif choice_numbers > max_numbers:
                    print(" " * 7, " * Enter a number between {} and {} * ".format(self.int_bet, max_numbers))
                else:
                    print(" * You cannot play {} numbers, because you chose {} *".format(choice_numbers, self.bet))

            except ValueError:
                print(" " * 14, "* Enter a numeric value *")

    def print_ticket(self):
        PrintTable.ticket_table(self.city, self.bet, self.numbers)