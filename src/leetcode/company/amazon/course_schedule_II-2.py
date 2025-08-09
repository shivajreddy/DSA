from typing import List
from collections import defaultdict, deque

class Solution:
    """
    - Topological sorting algorithm to find a valid course order
    - List to track prerequisite counts for each course
    - Graph to map courses to their dependentsA
    - Starts with courses that have no prerequisites and processes them using a queue
    - As each course is processed, it decrements the prerequisite count for its 
    dependent courses, adding them to the queue when their count reaches zero.
    - If all courses are processed, it returns the course order; otherwise, 
    it returns an empty list, indicating a cycle in the prerequisites.

    Time : O(V + E)
    Space: O(V + E)
        - V is the number of courses (numCourses) E is the number of prerequisite pairs.
    """
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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

