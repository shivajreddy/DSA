"""
Heap for custom objects

"""
import heapq


class Heap:

    def __init__(self):
        self._pq = [None]  # 1-indexed array

    def push(self, num):
        pq = self._pq

        pq.append(num)
        idx = len(pq) - 1

        # method 1: swap both current and parent items
        while idx // 2 > 0 and pq[idx // 2] < pq[idx]:
            pq[idx], pq[idx // 2] = pq[idx // 2], pq[idx]
            idx = idx // 2

        # method 2: child takes parent's value, at end current idx takes new item
        # while idx // 2 > 0 and pq[idx // 2] < num:
        #     pq[idx] = pq[idx // 2]
        #     idx = idx // 2
        # pq[idx] = num

    def get_heap(self):
        return self._pq


'''
Add the following items to heap 1 by 1
[ 21, 12, -1, 13, 11 ]

The heap should be like this after adding all items
        21
       /  \
      13   -1
     /  \
    12   11
array representation: [21, 13, -1, 12, 11]
'''

heap = Heap()
heap.push(21)
heap.push(12)
heap.push(-1)
heap.push(13)
heap.push(11)

print(heap.get_heap())

"""
Dealing with custom objects, if we have a complex object such as the TestScore class below.
say we wanted to sort by the student_id field.
And let's assume that all student_ids will be unique. One approach would be to create a custom comparators for the
'TestScore' class as shown in below implementation


here is another easier solution that overriding the `==` ,`<`, `>` etc operators.

We can wrap each element in a tuple then add that to our heap.
What we do is make the first element of the tuple the variable that we want to compare.
See the 'TestScore2' for how we use student_id.
"""


class TestScore:
    def __init__(self,
                 student_name: str,
                 student_id: int,
                 student_score: int):
        self.name = student_name
        self.id = student_id
        self.score = student_score

    def __eq__(self, other: 'TestScore'):
        return self.id == other.id

    def __ne__(self, other: 'TestScore'):
        return self.id != other.id

    def __lt__(self, other: 'TestScore'):
        return self.id < other.id

    def __le__(self, other: 'TestScore'):
        return self.id <= other.id

    def __gt__(self, other: 'TestScore'):
        return self.id > other.id

    def __ge__(self, other: 'TestScore'):
        return self.id >= other.id

    # {student_name}:{student_id}:{student_score}
    def __repr__(self):
        return f"{{{self.name}:{self.id}:{self.score}}}"


class TestScore2:
    def __init__(self,
                 student_name: str,
                 student_id: int,
                 student_score: int):
        self.name = student_name
        self.id = student_id
        self.score = student_score

    def __repr__(self):
        return f"{{{self.name}:{self.id}:{self.score}}}"


students1 = [
    TestScore("amy", 12, 80),
    TestScore("bob", 13, 92),
    TestScore("carl", 10, 95),
    TestScore("sam", 14, 84),
    TestScore("igor", 7, 23),
    TestScore("max", 4, 58),
    TestScore("james", 2, 49),
]

students2 = [
    TestScore2("amy", 12, 80),
    TestScore2("bob", 13, 92),
    TestScore2("carl", 10, 95),
    TestScore2("sam", 14, 84),
    TestScore2("igor", 7, 23),
    TestScore2("max", 4, 58),
    TestScore2("james", 2, 49),
]

students1_heap = []
students2_heap = []
heapq.heapify(students1_heap)
heapq.heapify(students2_heap)

# method 1: using the comparison functions of the TestScore class
for student in students1:
    heapq.heappush(students1_heap, student)

# method 2: wrap each element in a tuple then add that to our heap
# first element in the tuple is used for comparison, ensure 1st item is comparable
for student in students2:
    heapq.heappush(students2_heap, (student.id, student))

if __name__ == "__main__":
    print(students1_heap)
    print(students2_heap)
