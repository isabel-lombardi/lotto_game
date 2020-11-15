class PrintOutput:
    max_len = 55

    @staticmethod
    def horizontal_line():
        print("+", end="")
        for x in range(PrintOutput.max_len):
            print("-", end="")
        print("+")

    @staticmethod
    def header(txt=""):
        PrintOutput.horizontal_line()
        print("|", txt.center(PrintOutput.max_len - 2), "|")
        PrintOutput.horizontal_line()

    print()


class PrintTable:
    len_column = 32
    txt = "Lotto Ticket"

    def __init__(self, city, bet, numb):
        self.city = city
        self.bet = bet
        self.numb = numb

    # print " +________+ "
    @staticmethod
    def h_line():
        print("+", end="")
        for x in range(PrintTable.len_column):
            print("-", end="")
        print("+")

    @staticmethod
    def ticket_table(city, bet, numb):
        print()
        print()
        PrintTable.h_line()

        print("|", PrintTable.txt.center(PrintTable.len_column - 1) + "|")  # +self.len_column - 2 + "|")
        PrintTable.h_line()
        list_str = ' '.join([str(elem) for elem in numb])
        city_column = 25 - len(city)
        bet_column = 26 - len(bet)
        numb_column = 29 - len(list_str)

        white_line = "|" + " " * PrintTable.len_column + "|"

        print(white_line)
        print("|" + " CITY: " + city + " " * city_column + "|")
        print(white_line)
        print("|" + " BET: " + bet + " " * bet_column + "|")
        print(white_line)
        print("|", " -" * 14, "  |")
        print(white_line)
        print("|", list_str, " " * numb_column, "|")
        print(white_line)
        PrintTable.h_line()
        print()


welcome_mex = "WELCOME TO THE LOTTO TICKET GENERATOR "
print_out = PrintOutput()
print_out.header(welcome_mex)
print()

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
