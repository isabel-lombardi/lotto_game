from lotto.lotto import Lotto
from argparse import ArgumentParser


def start(n):
    tickets_list = []

    if n == 0:
        quit()

    for ticket in range(n):
        ticket = Lotto()
        tickets_list.append(ticket)

    for n in range(len(tickets_list)):
        tickets_list[n].choose_city()
        tickets_list[n].choose_bet_type()
        tickets_list[n].choose_numbers()
        tickets_list[n].print_ticket()


if __name__ == '__main__':
    parser = ArgumentParser(description="Random lotto ticket generator")
    parser.add_argument("-n", "-number", type=int, help="Number of tickets to generate", choices=[0, 1, 2, 3, 4, 5])
    args = parser.parse_args()

    result = (start(args.n))


