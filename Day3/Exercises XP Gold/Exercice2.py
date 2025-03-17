import random

class MyList:
    def __init__(self, letters):
        self.letters = letters
    
    def get_reversed(self):
        return list(reversed(self.letters))
    
    def get_sorted(self):
        return sorted(self.letters)
    
    def generate_random_list(self):
        return [random.randint(0, 100) for _ in range(len(self.letters))]


my_list = MyList(["b", "a", "d", "c"])
print("Reversed:", my_list.get_reversed())
print("Sorted:", my_list.get_sorted())
print("Random List:", my_list.generate_random_list())
