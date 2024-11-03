from typing import List
from collections import defaultdict, deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # idx: course number, value: no.of pre-reqs
        arr = [0 for _ in range(numCourses)]

        courses = defaultdict(list)

        for a, b in prerequisites:
            arr[a] += 1
            courses[b].append(a)

        # Deque to hold all courses with out pre-reqs
        q = deque([])

        for count, i in enumerate(arr):
            if count == 0:
                q.append(i)

        print(arr)
        print(courses)
        print(q)

        res = []

        while q:
            c = q.popleft()
            res.append(c)
            for num in courses[c]:
                arr[num] -= 1
                if arr[num] <= 0:
                    q.append(num)

        print(res)
        return res if len(res) == numCourses else []


# TESTS --------
sol = Solution()

"""
numCourses = 2
prerequisites = [[1, 0]]
assert sol.findOrder(numCourses, prerequisites) == [0, 1]
"""


numCourses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
assert sol.findOrder(numCourses, prerequisites) == [0, 2, 1, 3]

"""
numCourses = 1
prerequisites = []
assert sol.findOrder(numCourses, prerequisites) == [0]
"""
