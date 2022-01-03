# our own for loop
def special_for(iterable):
    iterator = iter(iterable)

    while True:
        try:
            print(iterator)
            print(next(iterator))
        except StopIteration:
            break


special_for([1, 2, 3])


# our own range
class MyRange:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.current = first

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.last:
            tmp = self.current
            self.current += 1
            return tmp
        else:
            raise StopIteration


my_range = MyRange(90, 100)
for i in my_range:
    print(i)
