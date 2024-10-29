'''
Constraints:
    1 <= numCourses <= 2000
    0 <= prerequisites[i] <= numCourses * (numCourses - 1)
    len(prerequisites[i])  == 2
    0 <= ai, bi < numCourses
    ai != bi

Scope & Assumptions:
    - not concerned about taking the shortest path to finish a given course
    - goal is to finish all courses & return the path that would lead to taking all courses
    - there could be multiple paths, any of them could be the answer

Observations:
    - If there is no course without any dependencies then we can't finish all courses

Approach & Solution:
    a

    Walkthrough of example 1:
            4	[ [1,0],[2,0],[3,1],[3,2] ]

    data-structure where index is the course # and value is the no. of pre-reqs it needs
            0	0	0	0		<- num. of prerequisites for each course
            0	1	1	2

    data-structure to look up using key in O(1) i.e., key is the course #, 
    and value is a list of courses that this course serves as a prereq
            0: [ 1, 2 ]
            1: [ 3 ]
            2: [ 3 ]
            3: [  ]

    dequeue to hold all course # that do not have any more pre-reqs
        q =  [ 0 ]
    as long as there is a q i.e., there are courses that have no other pre-reqs
    remove these courses from the q, one by one
    for each course, look at the hashmap to find all the courses that depend on this
    for those deps.(courses that have this key as a prereq), reduce the prereq count by 1 
    after reducing count, if the new count is 0, add course to deque (cuz it has no prereqs)

Explanation:
    prereq_count:
    An array that tracks how many prerequisites each course has.
    For example, if prereq_count[2] == 1, it means course 2 has one prerequisite.

    course_to_dependents: 
    A graph (using a dictionary) that maps each course to the courses that depend on it.
    For instance, if course_to_dependents[3] = [1, 2], it means both course 1 and course 2 depend
    on course 3 being completed.

    BFS Traversal:
        - Start with courses that have no prerequisites (no_prereq_courses).
        - For each course, reduce the prerequisite count of all dependent courses.
        - Add courses with zero remaining prerequisites to the queue.

    Final Check: 
        - If all courses can be taken (i.e., len(course_order) == numCourses), return the order.
        - Otherwise, return an empty list indicating that it's impossible to finish all 
        courses (due to a cycle).

Time & Space Complexity:
    Time Complexity:
    - O(V + E), where V is the number of courses (numCourses) and E is the number of prerequisite pairs.
    - This is because we process each course and each edge in the graph once.
    Space Complexity:
    - O(V + E), as we store the graph and prerequisite counts.
'''

from typing import List
from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Finds the order in which courses should be taken given a list of 
        prerequisites.

        Args:
        numCourses (int): The total number of courses.
        prerequisites (List[List[int]]): A list of prerequisite pairs where 
        the first course depends on the second.

        Returns:
        List[int]: A list of courses in the order they should be taken, 
        or an empty list if it's impossible.
        """

        # Initialize a list to count prerequisites for each course
        prereq_count = [0] * numCourses

        # Initialize a graph that maps each course to its dependent courses
        course_to_dependents = defaultdict(list)

        # Populate the prerequisite count and graph
        for dependent, prereq in prerequisites:
            prereq_count[dependent] += 1
            course_to_dependents[prereq].append(dependent)

        # Queue to store courses with no prerequisites (courses that can be taken right away)
        no_prereq_courses = deque([i for i in range(numCourses) if prereq_count[i] == 0])

        # List to store the final order of courses
        course_order = []

        # Process the courses in topological order
        while no_prereq_courses:
            # Take the current course (with no remaining prerequisites)
            course = no_prereq_courses.popleft()
            course_order.append(course)

            # For each course that depends on the current course, reduce its prerequisite count
            for dependent in course_to_dependents[course]:
                prereq_count[dependent] -= 1

                # If the dependent course has no more prerequisites, add it to the queue
                if prereq_count[dependent] == 0:
                    no_prereq_courses.append(dependent)

        # All courses weren't finished
        if len(course_order) != numCourses:
            return []

        return course_order

