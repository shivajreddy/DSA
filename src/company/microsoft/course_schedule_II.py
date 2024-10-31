from typing import List
# from collections import defaultdict, deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []

        print(res)
        return res


# TESTS --------
sol = Solution()

numCourses = 2
prerequisites = [[1, 0]]
assert sol.findOrder(numCourses, prerequisites) == [0, 1]


numCourses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
assert sol.findOrder(numCourses, prerequisites) == [0, 2, 1, 3]

numCourses = 1
prerequisites = []
assert sol.findOrder(numCourses, prerequisites) == [0]
