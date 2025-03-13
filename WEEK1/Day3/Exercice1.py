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
          


C1=Cat("Sam",2)
C2=Cat("Siamo",3)
C3=Cat("JIN",5)