class Prize:
    def __init__(self, combination=0, amount=0):
        self.amount = amount
        self.combination = combination

    def check_combination(self, bet_int, numbers):

        """
        keys = numbers played
        value = result ('gross amount / combination)
        value [x] = type of bet

                     ambata - ambo - terno - quaterna - cinquina"""

        combinations = {1: [1],
                        2: [2, 1],
                        3: [3, 3, 1],
                        4: [4, 6, 4, 1],
                        5: [5, 10, 10, 5, 1],
                        6: [6, 15, 20, 15, 6],
                        7: [7, 21, 35, 35, 21],
                        8: [8, 28, 56, 70, 56],
                        9: [9, 36, 84, 126, 126],
                        10: [10, 45, 120, 210, 252]}

        for key, value in combinations.items():
            if len(numbers) == key:
                self.combination = value[bet_int - 1]
                return self.combination

    def check_amount(self, bet_int, numbers):
        """keys = numbers played
        value = res ('gross amount / combination)
        value [x] = type of bet
                           ambata - ambo - terno - quaterna - cinquina"""

        gross_winnings = {1: [11.23],
                          2: [5.61, 250],
                          3: [3.74, 83.33, 4500],
                          4: [2.80, 41.66, 1125, 120000],
                          5: [2.24, 25, 450, 24000, 6000000],
                          6: [1.87, 16.66, 225, 8000, 1000000],
                          7: [1.60, 11.90, 128.57, 3428.57, 285714.28],
                          8: [1.40, 8.92, 80.35, 1714.28, 107142.85],
                          9: [1.24, 6.94, 53.57, 952.38, 47619.04],
                          10: [1.12, 5.55, 37.50, 571.42, 23809.52]}

        for key, value in gross_winnings.items():
            if len(numbers) == key:
                bet_int -= 1
                self.amount = value[bet_int]
                return self.amount