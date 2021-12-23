# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Henry', 1)
cat2 = Cat('Whiskers', 21)
cat3 = Cat('Oreo', 3)


# 2 Create a function that finds the oldest cat
def find_oldest_cat(cats: list[Cat]):
    num_of_cats = len(cats)

    if num_of_cats == 0:
        return None

    oldest_cat = cats[0]

    if num_of_cats > 1:
        for i in range(1, num_of_cats):
            cat = cats[i]
            if cat.age > oldest_cat.age:
                oldest_cat = cat

    return oldest_cat


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

cats = [cat1, cat2, cat3]
my_oldest_cat = find_oldest_cat(cats)
print(f'The oldest cat is {my_oldest_cat.age} years old')
