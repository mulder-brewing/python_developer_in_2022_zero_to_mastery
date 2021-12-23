# 4 pillars of OOP
# 1. Encapsulation
# 2. Abstraction
#    public and private - there is no privacy in python, the underscore is only a visual cue for developers
# 3. Inheritance
# 4. Polymorphism
#    same method behaves differently depending on the object. like the attack method in wizard and archer

class PlayerCharacter:

    def __init__(self, name='Anonymous', age=0):
        self._name = name
        self._age = age

    def run(self):
        print('run')

    def speak(self):
        print(f'my name is {self._name}, and I am {self._age} years old')


player1 = PlayerCharacter('Hank', 75)
player1.speak()


# Inheritance
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    @staticmethod
    def sign_in():
        print('logged in')

    def greet(self):
        print(f'hello!  my name is {self.name}, my email is {self.email}')

    def attack(self):
        print('attacking...')


class Wizard(User):
    def __init__(self, name, email, power):
        User.__init__(self, name, email)
        self.power = power

    def attack(self):
        # one way to call super method
        User.attack(self)
        print(f'attacking with power of {self.power}')

    def cloak(self):
        print(f'{self.name} has become invisible')


class Archer(User):
    def __init__(self, name, email, num_arrows):
        User.__init__(self, name, email)
        self.num_arrows = num_arrows

    def attack(self):
        # another way to call super method
        super().attack()
        print(f'attacking with arrows: arrows left {self.num_arrows}')

    def check_arrows(self):
        print(f'{self.num_arrows} left')


class HybridBorg(Wizard, Archer):
    def __init__(self, name, email, power, num_arrows):
        Wizard.__init__(self, name, email, power)
        Archer.__init__(self, name, email, num_arrows)


wizard = Wizard('Gandolph', 'gdolph@mail.com', 50)
wizard.sign_in()
wizard.attack()
wizard.greet()

archer1 = Archer('Arrow', 'arrow@mail.com', 40)
archer1.attack()

print('\n ----------- Multiple Inheritance ------------')
hb1 = HybridBorg('Borg', 'borg@mail.com', 77, 44)
print(hb1.greet())
hb1.check_arrows()
hb1.cloak()
hb1.attack()

print()

# isinstance
print(isinstance(wizard, object))
print(isinstance(wizard, Wizard))
print(isinstance(wizard, User))
print(isinstance(wizard, Archer))

# introspection - get all methods and attributes available
print(dir(wizard))


# dunder methods - sometimes dunder methods are meant to be overridden like __str__
class Toy:
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.parts = ['arms', 'legs', 'head']

    def __str__(self):
        return f'{self.color} toy that is {self.age} years old'

    def __len__(self):
        return 5

    def __call__(self, *args, **kwargs):
        return ('yess?')

    def __getitem__(self, item):
        return self.parts[item]


action_figure = Toy('red', 7)
print(action_figure)
print(len(action_figure))
# __call__ is interesting
print(action_figure())
print(action_figure[1])
