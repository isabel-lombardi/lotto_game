from lotto.lotto_helper import PrintsTicket, PrintOutput
from lotto.city import City
from lotto.bet_type import BetType


class PlayerInput:
    int_bet = 0

    @staticmethod
    def choose_city():
        PrintOutput.horizontal_line("  > Choose the 'ruota' based on the name of the city < ")
        PrintsTicket.table_choose_city()

        while True:
            try:
                city = int(input(" - Enter the number corresponding to the city: "))
                if City.is_city_valid(city):
                    c = City(city)
                    city = c.city_index(city)
                    return city
                else:
                    PrintsTicket.print_txt("*Enter a number between 1 to 10*")

            except ValueError:
                PrintsTicket.print_txt("* Enter the number corresponding to the city, not the name * ")

    @staticmethod
    def choose_bet_type():

        PrintOutput.horizontal_line(" > Enter the type of bet to apply for the ticket < ")
        PrintsTicket.table_choose_bet_type()

        while True:
            try:
                bet_type = int(input(" - Enter the number corresponding to the type of bet: "))
                if BetType.is_bet_type_valid(bet_type):
                    PlayerInput.int_bet += bet_type
                    b = BetType(bet_type)
                    bet_type = b.name_from_index(bet_type)
                    return bet_type
                else:
                    PrintsTicket.print_txt("*Enter a number between 1 to 5*")

            except ValueError:
                PrintsTicket.print_txt("* Enter the number corresponding to the type of bet, not the name * ")

    @staticmethod
    def choose_numbers():
        max_numbers = 10
        bet_type = BetType.bet_types[PlayerInput.int_bet - 1]

        PrintOutput.horizontal_line(" > You can play from {} to {} numbers < ".format(PlayerInput.int_bet, max_numbers))

        while True:
            try:
                numbers = int(input(" - How many numbers do you want to play?: "))
                if PlayerInput.int_bet <= numbers <= max_numbers:
                    return numbers

                elif numbers > max_numbers:
                    PrintsTicket.print_txt(" * Enter a number between {} and {} * ".format(PlayerInput.int_bet,
                                                                                           max_numbers))

                else:
                    PrintsTicket.print_txt(
                        " * You cannot play {} numbers, because you chose {} *".format(numbers, bet_type))

            except ValueError:
                PrintsTicket.print_txt("*Enter a numeric value*")

    @staticmethod
    def choose_played():
        PrintOutput.horizontal_line("> Enter an amount between 1€ and 200€ <")

        while True:
            try:
                played = float(input(" - How much do you want to play on the ticket?: "))

                if 1 <= played <= 200:
                    if played % 0.50 == 0:
                        return played
                    else:
                        PrintsTicket.print_txt("Bet can be increased with multiples of 0.50 cents")

                else:
                    PrintsTicket.print_txt("*Enter an amount between 1€ and 200€*")

            except ValueError:
                PrintsTicket.print_txt("*Enter a numeric value*")
