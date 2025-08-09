"""
Week 1: Python Fundamentals, OOP
"""

'''
List Comprehension
'''
my_list = [x for x in range(5)]
# print(my_list)

string_numbers = [str(x) for x in my_list]
# print(string_numbers)

even_numbers = [x for x in my_list if x % 2 == 0]
# print(even_numbers)


# * len(), del()
len(my_list)  # 5
sample_items = ["ball", 20, "red", True]
print(sample_items)  # ['ball', 20]

# ! this is invalid syntax
# result = del(sample_items[2:4])


'''
Zip
'''
names = ["same", "bob"]
ages = [21, 27]
names_and_ages = zip(names, ages)
# print(type(names_and_ages))			# <class 'zip'>
# print(list(names_and_ages))			# [('same', 21), ('bob', 27)]
# print(type(list(names_and_ages)[0]))	# <class 'tuple'>


'''
2D array
'''
N = 5
matrix = [[x for x in range(N)] for j in range(N)]
# print(matrix)


'''
Strings
'''
a = [[]] * 3  # [[], [], []]
a[1].append("hi")
# print(a)  # [['hi'], ['hi'], ['hi']]

b = [[] for _ in range(3)]  # [[], [], []]
b[0].append("hi")
# print(b)  # [['hi'], [], []]

'''
Sorting
'''
random_list = [5, 1, 3, 4, 2]
sorted_list = sorted(random_list)
reverse_sorted_list = sorted(random_list, reverse=True)


# print(random_list)  # [5, 1, 3, 4, 2]
# print(sorted_list)  # [1, 2, 3, 4, 5]
# print(reverse_sorted_list)  # [5, 4, 3, 2, 1]


# sorting objects based on keys
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return "Person[" + str(self.name) + "," + str(self.age) + "]"


bob = Person("bob", 21)
peter = Person("peter", 30)
shiva = Person("shiva", 27)
people = [bob, peter, shiva]
sorted_by_age_people = sorted(people, key=lambda p: p.age)
# print(people)  # [Person[bob,21], Person[peter,30], Person[shiva,27]]
# print(sorted_by_age_people)  # [Person[bob,21], Person[shiva,27], Person[peter,30]]

'''
Dictionary
{ key : value }
key -> only hashable data type
value -> any data type
'''
hm = {(1, 2): "can use tuple as key, since it's hashable"}
# print(hm[(1, 2)])  # can use tuple as key, since it's hashable

'''
Tuple
Tuple items are ordered, unchangeable, and allow duplicate values.
tuple_data_structure = ("one", 2, 5, True, None)
one_item_tuple = ("one",)  # must add  "," to tell interpreter that its Tuple not ()
'''

'''
Set
only hashable objects
A set is a collection which is unordered, unchangeable*, and un-indexed.
Note: Set items are unchangeable, but you can remove items and add new items.
'''

my_set = {10, 10, 20, "shiva", "reddy"}
single_item_set = {"hi"}
empty_set = set()  # 'set' is the built-in class
# print(my_set.__contains__(10))  # True
# print(100 in my_set)  # False
# print(my_set)  # {'shiva', 10, 20, 'reddy'}

even_set = {x for x in range(1, 10) if x % 2 == 0}  # {8, 2, 4, 6}
num_set = {x for x in range(5)}  # {0, 1, 2, 3, 4}

union_set = even_set.union(num_set)  # {0, 1, 2, 3, 4, 6, 8}
intersection_set = even_set.intersection(num_set)  # {2, 4}
difference_set = even_set.difference(num_set)  # {8, 6}

'''
Heap
'''
import heapq

arr = [10, 20, 30]
heap = []
for num in arr:
    heapq.heappush(heap, num)
# print(heap)

# If you have tuples, it will sort by the first element and use second element for ties.
my_heap = []
heapq.heappush(my_heap, (5, "write code"))
heapq.heappush(my_heap, (7, "release product"))
heapq.heappush(my_heap, (1, "write spec"))
heapq.heappush(my_heap, (3, "create tests"))

# print(my_heap)
# [(1, 'write spec'), (3, 'create tests'), (5, 'write code'), (7, 'release product')]

heapq.heappop(my_heap)  # (1, 'write spec')
# print(my_heap)  # [(3, 'create tests'), (7, 'release product'), (5, 'write code')]

# heap of fixed size
my_heap = []
max_size = 10
for x in range(20):
    # [9, 10, 11, 13, 12, 15, 14, 16, 18, 17, 19]
    # if len(my_heap) > max_size:
    #     heapq.heappop(my_heap)
    # heapq.heappush(my_heap, x)

    # or [9, 10, 12, 11, 13, 16, 15, 17, 14, 19, 18]
    if len(my_heap) > max_size:
        heapq.heappushpop(my_heap, x)
    else:
        heapq.heappush(my_heap, x)

'''
Deque
Deque is a Double linked list, with pop() and push() both taking O(1)
Operations: pop() -> removes & returns last element, popleft(), append(x) -> add x to right end, appendleft() 
'''
from collections import deque

empty_dq = deque()
dq = deque("shiva")
print(dq)
print(dq.append("x"))
print(dq)
