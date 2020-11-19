from random import sample
from lotto.city import City
from lotto.lotto_helper import PrintExtraction


class CheckExtraction:

    cities_extraction = {}

    def __init__(self, winning_numbers=""):
        self.winning_numbers = []

    for name in City.cities:
        cities_extraction[name] = sample(list(range(1, 90 + 1)), 5)
        cities_extraction = cities_extraction

    def print_extraction(self):
        PrintExtraction.extraction_table(self.cities_extraction)

    def is_winner(self, city, numbers):
        for key, value in CheckExtraction.cities_extraction.items():
            if city == key:
                self.winning_numbers = [n for n in numbers for ex_n in value if n == ex_n]
                return self.winning_numbers
            else:
                pass
