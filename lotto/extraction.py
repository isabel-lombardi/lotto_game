from random import sample
from lotto.city import City
from lotto.lotto_helper import PrintExtraction


class Extraction:

    cities_extraction = {}

    for name in City.cities[:-1]:
        cities_extraction[name] = sample(list(range(1, 90 + 1)), 5)

    def __init__(self):
        self.cities_extraction = Extraction.cities_extraction

    def print_extraction(self):
        PrintExtraction.extraction_table(self.cities_extraction)
