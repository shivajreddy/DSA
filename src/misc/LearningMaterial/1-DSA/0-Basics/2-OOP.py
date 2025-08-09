"""
Functions in python
"""


# initializer and class attributes


class Dog:
    # class attributes
    legs = 0

    def __init__(self, legs) -> None:
        self.legs = legs

    def __str__(self) -> str:
        return "Dog-legs:" + str(self.legs)

    # functions
    @staticmethod
    def speak():
        print("Dog?")

    def name(self, name):
        print("This dog's name is {}".format(name, self.legs))


class Cat:
    legs = 0

    def __init__(self, legs: int) -> None:
        self.legs = legs


my_dog = Dog(4)
# print(my_dog)

my_cat = Cat(3)


# my_dog.name("sunny")
# Dog.name(my_cat, "sunny")


# Note.: There are no true private variables or methods in Python like there are in Java.
# It is common convention to add an underscore to “mask” their true name. For example
class Dog:
    def __init__(self, name, age):
        # Underscores indicate private.
        self._name = name
        self._age = age

    __secretName = "bad doggo"


dog = Dog("sunny", 8)
print(dog._Dog__secretName)


# this works, but IDE also hints us that we are accessing private members
# print(dog._name)


# creating private members using "__", and accessing them
class PrivateMethod:
    def __init__(self):
        self.__secretKey = "MY_SOCIAL_SECURITY_NUMBER"

    def __privateMethod(self):
        return "SSN: " + self.__secretKey

    def privateMethod(self):
        return self.__privateMethod()


bankAcc = PrivateMethod()
print(bankAcc.privateMethod())  # -> SSN: MY_SOCIAL_SECURITY_NUMBER
# print(bankAcc.__privateMethod()) # fails with function not found error
# print(bankAcc.__secretKey) # fails with attribute not found error
print(bankAcc._PrivateMethod__privateMethod())  # -> SSN: MY_SOCIAL_SECURITY_NUMBER
print(bankAcc._PrivateMethod__secretKey)  # -> MY_SOCIAL_SECURITY_NUMBER

'''
Types -> Generic alias
'''
Type1 = list[int]
print(type(Type1))  # <class 'types.GenericAlias'>
Type2 = int
print(type(Type2))  # <class 'type'>


