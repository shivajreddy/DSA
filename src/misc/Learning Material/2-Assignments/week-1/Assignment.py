# ! 1. First have to ‘import time’ on line 1, to resolve line 19
import time


class Customer:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age


class LunchLine:
    def __init__(self, customers: list[Customer], time_end: int) -> None:
        self.time_end = time_end
        self.line_size = len(customers)
        self.customers = customers

    # ! naming the getter with a preset get_
    def get_line_size(self) -> int:
        return self.line_size

    def get_customers(self) -> list[Customer]:
        return self.customers

    def is_lunch_over(self) -> bool:
        current_time = time.time()
        if current_time > self.time_end:
            return True
        return False


c1 = Customer("Annie", 29)
c2 = Customer("Bob", 26)
c3 = Customer("Charlie", 29)
c4 = Customer("Dana", 35)
my_list = [c1, c2, c3, c4]

# lunchline = LunchLine(mylist, 24)
# ! 2. my_list not mylist, to resolve reference error
lunchline = LunchLine(my_list, 24)

# print(lunchline.line_size())
# ! 3. line_size is an attribute not a function, so it’s not callable, so change it to
print(lunchline.get_line_size())
print(lunchline.is_lunch_over())
for customer in lunchline.get_customers():
    print(customer)

