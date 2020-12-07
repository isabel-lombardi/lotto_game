from argparse import ArgumentParser
from lotto.lotto import Lotto
from lotto.extraction import Extraction
from lotto.player_input import PlayerInput
from lotto.lotto_helper import PrintOutput


def start(n):
    tickets = []

    if n == 0:
        quit()

    for sing_ticket in range(n):
        sing_ticket = PlayerInput()
        print()

        print("* Ticket {}".format(n))

        city = sing_ticket.choose_city()
        bet_type = sing_ticket.choose_bet_type()
        numbers = sing_ticket.choose_numbers()
        played = sing_ticket.choose_played()

        tickets.append(Lotto(city, bet_type, numbers, played))

    extraction = Extraction()
    extraction.print_extraction()

    for n in range(len(tickets)):
        print()
        print("* Ticket number: {}".format(n + 1))
        tickets[n].print_ticket()
        tickets[n].check_prize()
        print()


if __name__ == '__main__':
    parser = ArgumentParser(description="Random lotto ticket generator")
    parser.add_argument("-n", "-number", type=int, help="Number of tickets to generate", choices=[0, 1, 2, 3, 4, 5])
    args = parser.parse_args()

    tickets_numb = args.n

    if tickets_numb is None:
        PrintOutput.print_numbers_ticket(" > You can generate 1 to 5 tickets <")
        PrintOutput.print_numbers_ticket("0 to exit")

        while True:
            try:
                tickets_numb = int(input(" - How many tickets do you want to generate?: "))
                if 0 < tickets_numb <= 5:

                    break
                elif tickets_numb == 0:
                    quit()
                else:
                    PrintOutput.print_numbers_ticket("*Enter a number between 1 and 5*")

            except ValueError:
                PrintOutput.print_numbers_ticket("*Enter a numeric value*")

    start(tickets_numb)


