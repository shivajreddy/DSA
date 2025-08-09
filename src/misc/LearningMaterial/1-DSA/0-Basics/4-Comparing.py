from __future__ import annotations


class Person:

    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def __repr__(self):
        return f'{self._name}:{self._age}'

    # sorted checks for this "less than" function
    def __lt__(self, other: Person):
        if self.get_age() == other.get_age():
            return self.get_name() <= other.get_name()
        return self.get_age() < other.get_age()

    def __eq__(self, other: Person):
        return self._name == other.get_name()


# def __le__(self, other: Person):
#     if self.last_name == other.last_name:
#         return self.first_name <= other.first_name
#     return self.last_name < other.last_name


shiva = Person("shiva", 28)
q = Person("q", 28)
people = [shiva, q]
print(people)

sorted_people = sorted(people)
print(sorted_people)

print(shiva == q)
