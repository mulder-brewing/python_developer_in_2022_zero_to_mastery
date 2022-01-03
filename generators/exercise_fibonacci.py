class Fibonacci:
    def __init__(self, end_index):
        self.current_fib = 0
        self.last_fib = 0
        self.current_index = 0
        self.end_index = end_index

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index <= self.end_index:
            if self.current_index == 0:
                pass
            elif self.current_index == 1:
                self.current_fib = 1
            else:
                tmp = self.current_fib
                self.current_fib = self.last_fib + self.current_fib
                self.last_fib = tmp

            self.current_index += 1
            return self.current_fib
        else:
            raise StopIteration


for i in Fibonacci(20):
    print(i)
