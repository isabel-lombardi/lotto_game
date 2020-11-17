class City:
    cities = ["Bari", "Cagliari", "Firenze", "Genova", "Milano",
              "Napoli", "Palermo", "Roma", "Torino", "Venezia", "Tutte"]

    def __init__(self, city):
        if City.is_city_valid(city):
            self.city = City.city_index(city)
           # self.city = city
        else:
            pass

    @staticmethod
    def is_city_valid(city=""):
        for number, name in enumerate(City.cities, 1):
            if city == number:
                return True
            else:
                pass

    @staticmethod
    def city_index(city):
        for number, name in enumerate(City.cities, 1):
            if city == number:
                city = name
                return city


