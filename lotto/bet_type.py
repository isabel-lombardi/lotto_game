class BetType:
    bet_types = ["Ambata", "Ambo", "Terno", "Quaterna", "Cinquina"]

    def __init__(self, bet_type):

        if BetType.is_bet_type_valid(bet_type):
            self.bet_type = BetType.bet_index(bet_type)
            self.numbers_for_bet = [bet_type]
        else:
            pass

    @staticmethod
    def is_bet_type_valid(bet_type):
        for number, name in enumerate(BetType.bet_types, 1):
            if bet_type == number:
                return True
            else:
                pass

    @staticmethod
    def bet_index(bet_type):
        for number, name in enumerate(BetType.bet_types, 1):
            if bet_type == number:
                bet_type = name
                return bet_type
