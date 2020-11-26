from random import sample
from lotto.city import City
from lotto.lotto_helper import PrintExtraction


class Extraction:
    cities_extraction = {}

    for name in City.cities:
        cities_extraction[name] = sample(list(range(1, 90 + 1)), 5)

    def __init__(self):
        self.cities_extraction = Extraction.cities_extraction

    def print_extraction(self):
        PrintExtraction.extraction_table(self.cities_extraction)

    def is_winner(self, city, numbers):
        winning_numbers = []
        for key, value in self.cities_extraction.items():
            if city == key:
                winning_numbers = [n for n in numbers for ex_n in value if n == ex_n]
                return winning_numbers

            elif city == City.cities[-1]:
                for n in numbers:
                    for ex_n in value:
                        if ex_n == n:
                            winning_numbers.append(n)
                            return winning_numbers

            else:
                pass
