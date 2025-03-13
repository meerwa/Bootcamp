class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = {}

    def add_animal(self, animal, count=1):
        if animal in self.animals:
            self.animals[animal] += count
        else:
            self.animals[animal] = count

    def get_info(self):
        info = f"{self.name}'s farm\n\n"
        for animal, count in sorted(self.animals.items()):
            info += f"{animal} : {count}\n"
        info += "\n    E-I-E-I-0!\n"
        return info

    def get_animal_types(self):
        return sorted(self.animals.keys())

    def get_short_info(self):
        animal_types = self.get_animal_types()
        formatted_animals = [f"{a}s" if self.animals[a] > 1 else a for a in animal_types]
        return f"{self.name}'s farm has {', '.join(formatted_animals[:-1])} and {formatted_animals[-1]}."


macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.get_short_info())
