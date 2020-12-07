class BetType:
    bet_types = ["Ambata", "Ambo", "Terno", "Quaterna", "Cinquina"]

    def __init__(self, bet_type):

        if BetType.is_bet_type_valid(bet_type):
            self.bet_type = BetType.index_from_name(bet_type)
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
    def name_from_index(bet_type):
        for number, name in enumerate(BetType.bet_types, 1):
            if bet_type == number:
                bet_type = name
                return bet_type

    @staticmethod
    def index_from_name(bet_type):
        for number, name in enumerate(BetType.bet_types, 1):
            if bet_type == name:
                bet_type = number
                return bet_type
