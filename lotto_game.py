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
        print()
        print("* Ticket: {}".format(n + 1))
        print()
        tickets_list[n].choose_city()
        tickets_list[n].choose_bet_type()
        tickets_list[n].choose_numbers()

    for n in range(len(tickets_list)):
        print()
        print("* Ticket number: {}".format(n + 1))
        tickets_list[n].print_ticket()


if __name__ == '__main__':
    parser = ArgumentParser(description="Random lotto ticket generator")
    parser.add_argument("-n", "-number", type=int, help="Number of tickets to generate", choices=[0, 1, 2, 3, 4, 5])
    args = parser.parse_args()

    tickets_numb = args.n

    if tickets_numb is None:
        print()
        print("{:^57}\n{:^57}".format(" > You can generate 1 to 5 tickets <", "0 to exit"))

        print()

        while True:
            tickets_numb = int(input(" - How many tickets do you want to generate?: "))
            if 0 < tickets_numb <= 5:

                break
            elif tickets_numb == 0:
                quit()
            else:
                print("{:^57}".format("*Enter a number between 1 and 5*"))
    start(tickets_numb)
