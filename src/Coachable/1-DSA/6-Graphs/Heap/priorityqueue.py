"""
Heap
"""
from typing import List


class MaxPriorityQueue:
    # creates a max priority queue
    def __init__(self):
        self.arr = [None]  # 1-indexed array, so use 'None' at 0 index

    # inserts a key into the priority queue
    def insert(self, key: int) -> None:
        """
        :param key : the new number that has to be inserted in to the heap
        :type key: Integer for now
        :return : doesn't return anything, simply adds the given number to heap
        :rtype : None
        """
        pq = self.arr
        pq.append(key)  # add the new item to the pq

        # swimming -> log(n)
        idx = len(pq) - 1  # idx points to the newly added key

        # idx -> points to the last node in the tree
        # idx // 2 -> idx of parent_node for the node at idx
        while idx // 2 > 0 and pq[idx // 2] < pq[idx]:
            pq[idx // 2], pq[idx] = pq[idx], pq[idx // 2]
            idx = idx // 2

    # return and remove the largest key
    def delete(self):
        """
        make sure pq has at least 1 item to remove
        :return: the top item in the priority queue
        :rtype: returns int for now
        """

        assert not self.isEmpty()
        arr = self.arr

        # swap the 1st item and last item
        arr[1], arr[len(arr) - 1] = arr[len(arr) - 1], arr[1]

        val = arr.pop()

        # sinking -> log(n)
        idx = 1
        while idx * 2 < len(arr):
            curr = arr[idx]
            left = arr[idx * 2]
            right = float('-inf')
            # if there is a right child, then right points to that
            if idx * 2 + 1 < len(arr):
                right = arr[idx * 2 + 1]
            if curr >= left and curr >= right:  # finished sinking
                continue
            if left > curr:
                arr[idx], arr[idx * 2] = arr[idx * 2], arr[idx]
                idx = idx * 2
            else:
                arr[idx], arr[idx * 2 + 1] = arr[idx * 2 + 1], arr[idx]
                idx = idx * 2 + 1
        return val

    # returns the largest key
    def get_max(self) -> int | None:
        assert not self.isEmpty()
        return self.arr[1]

    # returns a boolean indicating if the priority queue empty
    def isEmpty(self):
        return len(self.arr) == 1

    # returns the number of keys in the priority queue
    def size(self):
        return len(self.arr) - 1


if __name__ == "__main__":
    arr = [21, 13, -1, 12, 11]
    pq = MaxPriorityQueue()

    for num in arr:
        pq.insert(num)
    print(pq.arr)

    for _ in arr:
        print(pq.delete())
