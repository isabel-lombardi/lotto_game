from datetime import date
from lotto.city import City
from lotto.bet_type import BetType


class PrintOutput:
    max_len = 55

    @staticmethod
    def horizontal_line(txt=""):

        if txt:
            print()
            print(txt.center(PrintOutput.max_len - 2))

        print("+", end="")
        for x in range(PrintOutput.max_len):
            print("-", end="")
        print("+")

    @staticmethod
    def header(txt=""):
        PrintOutput.horizontal_line()
        print("|", txt.center(PrintOutput.max_len - 2), "|")
        PrintOutput.horizontal_line()

    @staticmethod
    def print_numbers_ticket(txt):
        print()
        print("{:^57}".format(txt))
        print()


class PrintTable:
    width_column = 32
    txt = "Lotto Ticket"

    # print " +------+ "
    @staticmethod
    def h_line():
        print("+", end="")
        for x in range(PrintTable.width_column):
            print("-", end="")
        print("+")

    @staticmethod
    def ticket_table(city, bet, numb, played):
        PrintTable.h_line()

        print(("|{:^32}|".format("Lotto Ticket")))
        PrintTable.h_line()

        list_str = ' '.join([str(elem) for elem in numb])
        city_column = 25 - len(city)
        bet_column = 26 - len(bet)
        numb_column = 29 - len(list_str)
        play_column = 21 - len(str(played))

        white_line = "|{}|".format(" " * PrintTable.width_column)

        print(white_line, "\n| CITY: {}{}|".format(city, " " * city_column))
        print(white_line, "\n| BET: {}{}|".format(bet, " " * bet_column))
        print(white_line, "\n| AMOUNT: {}€{} |".format(played, " " * play_column))
        print(white_line, "\n| {} |".format(" - " * 10))
        print(white_line, "\n| {} {} |".format(list_str, " " * numb_column))
        print(white_line)
        PrintTable.h_line()
        print()


class PrintExtraction:
    width_column = 32

    @staticmethod
    def extraction_table(extraction):
        print()
        print()
        txt = " L O T T O"

        today = date.today()
        tod_date = today.strftime("%d/%m/%Y")  # dd/mm/YY

        print(txt.center(PrintExtraction.width_column))
        PrintTable.h_line()
        print("  {}\n  {}".format("Extraction of:", tod_date))
        PrintTable.h_line()

        for name, numbers in extraction.items():
            if len(name) < 9:
                name_space = 11 - len(name)

                n = ["%02d" % x for x in numbers]
                print("| ", name, " " * name_space, " ".join(map(str, n)), " " * 1, "|")
        PrintTable.h_line()


welcome_mex = "WELCOME TO THE LOTTO TICKET GENERATOR "
print_out = PrintOutput()
print_out.header(welcome_mex)


class PrintsTicket:

    @staticmethod
    def print_txt(txt):
        print()
        print("{:^55}".format(txt))
        if len(txt) > 55:
            print(txt)

    @staticmethod
    def print_winning(bet, winning_numbers, win, total_win):
        print("{:^33}\n{:^33}".format("CONGRATULATIONS", "*YOU WIN*"))
        print("With {} on the numbers: \n{:^33}".format(bet, " ".join(map(str, winning_numbers))))
        print()

        if win <= 500:
            print("TOTAL WIN: {:.2f}€".format(win))
        else:
            print("Gross win: {}".format(win))
            print("TOTAL WIN: {:.2f}€".format(total_win))

    @staticmethod
    def print_loser():
        print("{:^33}\n{:^33}".format("The ticket is not winning, try again", ">But play responsibly<"))

    @staticmethod
    def table_choose_city():
        for x, name in enumerate(City.cities, 1):
            print(" -", x, ":", name)
        PrintOutput.horizontal_line()

    # ---------------------------------

    @staticmethod
    def table_choose_bet_type():
        for x, name in enumerate(BetType.bet_types, 1):
            print(" -", x, ":", name)
        PrintOutput.horizontal_line()

    # ----------------------------------


"""

Example of a ticket:

+--------------------------------+
|           Lotto Ticket         |
+--------------------------------+
|                                |
| CITY: Cagliari                 |
|                                |
| BET: Ambo                      |
|                                |
|  - - - - - - - - - - - - - -   |
|                                |
| 10 81                          |
|                                |
+--------------------------------+


"""
