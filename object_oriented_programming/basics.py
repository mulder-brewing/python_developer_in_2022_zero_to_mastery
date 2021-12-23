class BigObject:
    pass


print(type(BigObject))
obj1 = BigObject()
print(type(obj1))


# Create our own real class
class PlayerCharacter:
    # Class Attribute (static)
    membership = True

    def __init__(self, name='Anonymous', age=0):
        self.name = name
        self.age = age

    def shout(self):
        print(f'my name is {self.name} and I am {self.age} years old')

    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2

    @classmethod
    def get_anonymous_instance(cls):
        return cls()

    @staticmethod
    def i_am_static():
        print('i am static')


player1 = PlayerCharacter('Master Chief', 254)
player1.shout()
player1.name = 'Blah'
print(player1.name)
player1.__setattr__('power', 'killing covenant')
player1.weapon = 'BR'
print(player1.power)
print(player1.weapon)

help(player1)

print(player1.membership)
# can be overriden for the instance, which is weird
player1.membership = False
print(player1.membership)
player2 = PlayerCharacter('P2', 66)
print(player2.membership)
print(PlayerCharacter.membership)

anonymous_player = PlayerCharacter.get_anonymous_instance()
anonymous_player.shout()
print(anonymous_player.adding_things(2, 3))
print(PlayerCharacter.adding_things(2, 3))
anonymous_player.i_am_static()
