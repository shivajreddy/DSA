from __future__ import annotations

'''
Tour class which is a collection of ordered points.
The functions allow you to insert points in a way that will 
keep the distance of the tour as small as possible.
Each Tour object should be able to print out the points in order, 
count its number of points, compute its total distance, 
and insert a new point using either of the two heuristics. 
The constructor creates an empty tour.
'''

from point import Point


# Hint: You will want to use a classic LinkedList Node to implement the tour.
class Node:
    def __init__(self, point):
        self.point = point  # This node's point
        self.next = None  # The next node


class Tour:
    # Creates an empty tour
    # Initialize any instance variables you think are needed.
    def __init__(self):
        self._start = None  # this will hold the node whose value is a point object
        self._distance = 0
        self._total_points = 0  # the number of points in the tour
        self._total_distance = 0  # total distance between each of the points in the tour

    # Returns string representation of the Tour.
    # Should output a list of all points on the Tour.
    def __str__(self):
        result = []
        curr = self._start
        while curr:
            result.append(str(curr.point))
            curr = curr.next
        return str(result)

    # return the number of points on tour
    # Hint: You should not have to iterate through the entire Tour to get the size.
    def size(self):
        return self._total_points

    # Computers and returns the distance of entire tour
    def distance(self):
        if not self._start:
            return 0
        total_distance = 0
        prev, curr = self._start, self._start
        while curr:
            dist = curr.point.distance_to(prev.point)
            total_distance += dist
            prev = curr
            curr = curr.next
        # should join last to first
        dist = prev.point.distance_to(self._start.point)
        total_distance += dist
        # print("totalsize = ", self.size(), " tour=", self)
        print(total_distance, "has circular:", self.has_circular())
        return total_distance

    # Helper function to insert a new point p into the Tour after a previous Node prev.
    # Example if the tour is a -> b -> c -> d
    # And you call _insert_at(p, c). Then the Tour should look like.
    # a -> b -> c -> p -> d
    # You can use this helper function in the insertNearest and insertSmallest
    # once you find the point you should insert p after.
    def _insert_at(self, p: Point, prev: Node):
        nxt = prev.next
        new_node = Node(p)  # create a new node, and its next node is nxt
        prev.next = new_node
        new_node.next = nxt

    # Insert a new Point p to the Tour using neearest neighbor heuristic
    def insert_nearest(self, p: Point):
        curr = self._start
        if not curr:
            self._start = Node(p)
            self._total_points += 1
            return

        smallest_dist = float('inf')
        smallest_dist_node = None
        while curr:
            dist = curr.point.distance_to(p)
            if dist < smallest_dist:
                smallest_dist = dist
                smallest_dist_node = curr
                # print(f"dist={dist}")
            curr = curr.next
        self._insert_at(p, smallest_dist_node)
        self._total_points += 1
        # print(f"total dist now is:{self.distance()}")
        # print("end insert_smallest")

    # Insert a new Point p to the Tour using smallest increase heuristic
    def insert_smallest(self, p: Point):
        if not self._start:
            self._start = Node(p)
            self._total_points += 1
            return

        prev, curr = self._start, self._start
        smallest_total_dist = float('inf')
        smallest_node = None
        while curr:
            if p == prev.point or p == curr.point:
                self._total_points += 1
                return
            dist_prev_curr = curr.point.distance_to(prev.point)
            dist_prev_new = prev.point.distance_to(p)
            dist_new_curr = curr.point.distance_to(p)
            new_total_dist = dist_prev_new + dist_new_curr - dist_prev_curr
            if new_total_dist < smallest_total_dist:
                smallest_total_dist = new_total_dist
                smallest_node = prev
            prev = curr
            curr = curr.next

        # finally check if the new node should be placed b/w the tail and head
        dist_last_first = prev.point.distance_to(self._start.point)
        dist_last_new = prev.point.distance_to(p)
        dist_new_first = self._start.point.distance_to(p)
        d = dist_last_new + dist_new_first - dist_last_first
        if d < smallest_total_dist:
            smallest_node = prev

        self._insert_at(p, smallest_node)
        self._total_points += 1
        # if self.distance() >= 4000:
        # print("self._total_distance=", self.distance())
        # print(self)

    def has_circular(self):
        dummy = Node(None)
        dummy.next = self._start
        slow, fast = dummy, dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
