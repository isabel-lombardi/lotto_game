from random import sample

from lotto.city import City
from lotto.bet_type import BetType
from lotto.lotto_helper import PrintOutput, PrintTable
from lotto.check_extraction import CheckExtraction


class Lotto:

    def __init__(self, city="", bet="", numbers=""):
        self.city = city
        self.bet = bet
        self.int_bet = 0
        self.numbers = numbers
        self.winning_numbers = []

    def choose_city(self):
        print()
        choice_mex = " > Choose the 'ruota' based on the name of the city <"
        PrintOutput.horizontal_line(choice_mex)
        print()

        for x, name in enumerate(City.cities, 1):
            print(" -", x, ":", name)
        PrintOutput.horizontal_line()

        while True:
            try:
                city_choice = int(input(" - Enter the number corresponding to the city: "))

                if City.is_city_valid(city_choice):
                    c = City(city_choice)
                    self.city = c.city_index(city_choice)
                    break
                else:
                    print("{:^55}".format("*Enter a number between 1 to 10*"))

            except ValueError:
                print("* Enter the number corresponding to the city, not the name * ")

    def choose_bet_type(self):
        print()
        choice_mex = " > Enter the type of bet to apply for the ticket < "
        PrintOutput.horizontal_line(choice_mex)

        for x, name in enumerate(BetType.bet_types, 1):
            print(" -", x, ":", name)
        PrintOutput.horizontal_line()

        while True:
            try:
                bet_choice = int(input(" Enter the number corresponding to the type of bet: "))

                if BetType.is_bet_type_valid(bet_choice):
                    self.int_bet = bet_choice
                    b = BetType(bet_choice)
                    self.bet = b.bet_index(bet_choice)
                    break
                else:
                    print("{:^55}".format("*Enter a number between 1 to 5*"))
            except ValueError:
                print("* Enter the number corresponding to the type of bet, not the name * ")

    def choose_numbers(self):
        max_numbers = 10

        print()
        choice_mex = "> You can play from {} to {} numbers <".format(self.int_bet, max_numbers)
        PrintOutput.horizontal_line(choice_mex)

        while True:
            try:
                choice_numbers = int(input(" - How many numbers do you want to play?: "))

                if self.int_bet <= choice_numbers <= max_numbers:
                    self.numbers = (sample(list(range(1, 90 + 1)), choice_numbers))
                    break
                elif choice_numbers > max_numbers:
                    print(" " * 7, " * Enter a number between {} and {} * ".format(self.int_bet, max_numbers))
                else:
                    print(" * You cannot play {} numbers, because you chose {} *".format(choice_numbers, self.bet))

            except ValueError:
                print("{:^55}".format("*Enter a numeric value*"))

    def print_ticket(self):
        PrintTable.ticket_table(self.city, self.bet, self.numbers)

    def check_win(self):
        check_win = CheckExtraction()
        self.winning_numbers = check_win.is_winner(self.city, self.numbers)
        if len(self.winning_numbers) >= self.int_bet:
            print("{:^33}\n{:^33}".format("CONGRATULATIONS", "*YOU WIN*"))
            print("With {} on the numbers: \n{:^33}".format(self.bet, " ".join(map(str, self.winning_numbers))))
            return True

        else:
            print("{:^33}\n{:^33}".format("The ticket is not winning, try again", ">But play responsibly<"))
            pass

