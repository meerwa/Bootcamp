class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

def find_oldest_cat(cats):
    oldest_cat = None
    max_age = 0

    for cat in cats:
        if cat.age > max_age:
            max_age = cat.age
            oldest_cat = cat

    return oldest_cat

# Instantiate Cat objects
C1 = Cat("Sam", 2)
C2 = Cat("Siamo", 3)
C3 = Cat("JIN", 5)

# Create a list of the cat objects
cats = [C1, C2, C3]

# Find the oldest cat
oldest_cat = find_oldest_cat(cats)

# Print the result
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")