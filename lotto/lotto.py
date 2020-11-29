from random import sample

from lotto.city import City
from lotto.bet_type import BetType
from lotto.lotto_helper import PrintOutput, PrintTable
from lotto.check_extraction import Extraction
from lotto.prize import Prize


class Lotto:

    def __init__(self, city="", bet="", numbers="", played=0):
        self.city = city
        self.bet = bet
        self.int_bet = 0
        self.numbers = numbers
        self.played = played
        self.winning_numbers = []

    def choose_city(self):
        print()
        choice_mex = "  > Choose the 'ruota' based on the name of the city < "
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
        choice_mex = " > Enter the type of bet to apply for the ticket < "
        print()
        PrintOutput.horizontal_line(choice_mex)

        for x, name in enumerate(BetType.bet_types, 1):
            print(" -", x, ":", name)
        PrintOutput.horizontal_line()

        while True:
            try:
                bet_choice = int(input(" - Enter the number corresponding to the type of bet: "))
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
        choice_mex = " > You can play from {} to {} numbers < ".format(self.int_bet, max_numbers)
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

    def choose_played(self):
        print()
        choice_mex = "> Enter an amount between 1€ and 200€ <"
        PrintOutput.horizontal_line(choice_mex)
        while True:
            try:
                played_choice = float(input(" - How much do you want to play on the ticket?: "))

                if 1 <= played_choice <= 200:
                    self.played = played_choice
                    break
                else:
                    print("{:^55}".format("*Enter an amount between 1€ and 200€*"))

            except ValueError:
                print("{:^55}".format("*Enter a numeric value*"))

    def print_ticket(self):
        PrintTable.ticket_table(self.city, self.bet, self.numbers, self.played)

    def check_win(self):
        check_win = Extraction()
        self.winning_numbers = check_win.is_winner(self.city, self.numbers)
        if len(self.winning_numbers) >= self.int_bet:
            print("{:^33}\n{:^33}".format("CONGRATULATIONS", "*YOU WIN*"))
            print("With {} on the numbers: \n{:^33}".format(self.bet, " ".join(map(str, self.winning_numbers))))
            return True

        else:
            print("{:^33}\n{:^33}".format("The ticket is not winning, try again", ">But play responsibly<"))
            pass

    def check_prize(self):
        max_win = 6000000
        if Lotto.check_win(self) is True:

            p = Prize()
            combination = p.check_combination(self.int_bet, self.winning_numbers)
            amount = p.check_amount(self.int_bet, self.numbers)

            tax = 0.08  # 8%
            print()

            if self.city == City.cities[-1]:
                amount /= 10

            win = self.played * combination * amount

            if win <= 500:
                print("TOTAL WIN: {:.2f}€".format(win))
            else:
                print("Gross win: {}".format(win))
                net_total = win * tax
                total_win = win - net_total
                if total_win > max_win:
                    total_win = max_win
                    print("TOTAL WIN: {:.2f}€".format(total_win))