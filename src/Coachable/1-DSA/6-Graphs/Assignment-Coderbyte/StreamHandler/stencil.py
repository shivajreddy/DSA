from __future__ import annotations
import heapq

'''
Complete the StreamHandlerKLargest class that has a capacity k by filling in the methods.
'''


class StreamHandlerKLargest:

    def __init__(self, k: int) -> None:
        self.k = k
        self.pq = []  # using an empty array, since using heapq API for building heap
        heapq.heapify(self.pq)

    '''
    This method adds the stream element to the collection. 
    You only need to store the k largest elements seen so far at any given point in time.
    '''

    def add_stream_element(self, e: int) -> None:
        # if limit is reached then remove the smallest of all
        if self.k == len(self.pq):
            smallest_element = heapq.heappop(self.pq)
            # if new element is even smaller that smallest element in heap,
            # then disregard new element
            if e < smallest_element:
                e = smallest_element
        heapq.heappush(self.pq, e)

    ''' 
    This method returns the k largest elements seen so far.
    '''

    def k_largest(self) -> list[int]:
        result = []
        for _ in range(len(self.pq)):
            item = heapq.heappop(self.pq)
            result.append(item)
        return result


'''
Complete the StreamHandlerKSmallest class that has a capacity k by filling in the methods.
'''


class StreamHandlerKSmallest:
    def __init__(self, k: int) -> None:
        self.k = k
        self.pq = []  # using an array, since using the heapq API for building heap
        # since python builtin has min-heap, we input element e as -e, for max-heap
        heapq.heapify(self.pq)

    '''
    This method adds the stream element to the collection. 
    You only need to store the k smallest elements seen so far at any given point in time.
    '''

    def add_stream_element(self, e: int) -> None:
        if self.k == len(self.pq):
            biggest_element = -heapq.heappop(self.pq)
            if e > biggest_element:
                e = biggest_element
        heapq.heappush(self.pq, -e)

    ''' 
    This method returns the k smallest elements seen so far.
    '''

    def k_smallest(self) -> list[int]:
        result = []
        for _ in range(len(self.pq)):
            item = heapq.heappop(self.pq)
            result.append(-item)
        return result


''' 
Write a function that creates a copy of the list, and sorts it in ascending order
using a heap.
'''


def heapsort(input_list: list[int]) -> list[int]:
    pq = []
    heapq.heapify(pq)
    for num in input_list:
        heapq.heappush(pq, num)

    result = []
    while pq:
        smallest_item = heapq.heappop(pq)
        result.append(smallest_item)
    return result


'''
Suppose we have some data that can be expressed as a tuple (a, b, c). 
We want to get the top k tuples out of a collection of n total tuples, 
where k <= n. Each datapoint has a score, defined as 2*a + 5*b + 10*c, 
and the higher the score, the greater the datapoint. 
Complete the class for this datapoint object, and complete the below function, using a heap to do so.
'''


class Datapoint:
    def __init__(self, a: int, b: int, c: int) -> None:
        self.a = a
        self.b = b
        self.c = c

    def to_tuple(self) -> tuple[int, int, int]:
        return (self.a, self.b, self.c)

    # returns the score using the given formula: 2*a + 5*b + 10*c
    def score(self) -> int:
        score = 2 * self.a + 5 * self.b + 10 * self.c
        return score

    # returns a tuple with 1st item as score of this data point, and 2nd item as DataPoint instance
    def to_score_tuple(self) -> tuple[int, 'DataPoint']:
        score_tuple = (self.score(), self)
        return score_tuple


# Return them as tuples, using the to_tuple method in the Datapoint class.
def get_top_k_datapoints(data_collection: list[Datapoint], k: int) -> set[tuple[int, int, int]]:
    # create a min-heap to store special objects i.e., score_tuple's
    # where 1st item i.e, score of the datapoint is used to compare the priority, and 2nd item
    # is the DataPoint instance itself
    pq = []
    heapq.heapify(pq)

    # go through the collection and add the datapoint object in tuple form, into the min-heap
    for data_point in data_collection:
        # if the limit of heap is reached, pop the smallest item
        if len(pq) == k:
            smallest_score_tuple = heapq.heappop(pq)  # we get items in the type tuple[int, DataPoint]
            # compare the smallest item in heap with the new item, and keep the largest of both.
            if data_point.score() < smallest_score_tuple[0]:
                data_point = smallest_score_tuple[1]
        heapq.heappush(pq, data_point.to_score_tuple())

    result = set()
    # start by popping each item from min-heap, which gives the item with lowest priority at a given time
    for _ in range(len(pq)):
        score_tuple = heapq.heappop(pq)
        result.add(score_tuple[1].to_tuple())  # add this object to the result in tuple form

    return result
