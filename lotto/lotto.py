from random import sample

from lotto.city import City
from lotto.bet_type import BetType
from lotto.lotto_helper import PrintTable, PrintsTicket
from lotto.extraction import Extraction
from lotto.prize import Prize


class Lotto:

    def __init__(self, city="", bet="", numbers="", played=0):
        self.city = city
        self.bet = bet
        self.int_bet = BetType.index_from_name(self.bet)
        self.numbers = Lotto.gen_random_numbers(numbers)

        self.played = played
        self.winning_numbers = []

    @staticmethod
    def gen_random_numbers(numbers):
        numbers = sample(list(range(1, 90 + 1)), numbers)
        return numbers

    def print_ticket(self):
        PrintTable.ticket_table(self.city, self.bet, self.numbers, self.played)

    def check_win(self):
        extraction = Extraction()

        for key, value in extraction.cities_extraction.items():
            if self.city == key:
                winning_numbers = [n for n in self.numbers for ex_n in value if n == ex_n]
                self.winning_numbers = winning_numbers

            # if city = "Tutte"
            if self.city == City.cities[-1]:
                winning = {}
                for city in extraction.cities_extraction.keys():
                    win_numb = [n for n in self.numbers if n in extraction.cities_extraction[city]]
                    winning[city] = win_numb

                for city in winning.keys():
                    if len(winning[city]) >= self.int_bet:
                        self.winning_numbers = winning[city]

            else:
                pass

        if len(self.winning_numbers) >= self.int_bet:
            return True

        else:
            PrintsTicket.print_loser()
            pass

    def check_prize(self):
        max_win = 6000000
        if Lotto.check_win(self) is True:

            p = Prize()
            combination = p.check_combination(self.int_bet, self.winning_numbers)
            amount = p.check_amount(self.int_bet, self.numbers)

            tax = 0.08  # 8%

            if self.city == City.cities[-1]:
                amount /= 10

            win = self.played * combination * amount

            net_total = win * tax
            total_win = win - net_total
            if total_win > max_win:
                total_win = max_win

            PrintsTicket.print_winning(self.bet, self.winning_numbers, win, total_win)