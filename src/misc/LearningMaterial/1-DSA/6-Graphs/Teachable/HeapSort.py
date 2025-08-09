class MaxPriorityQueue:
    # creates a max priority queue
    def __init__(self):
        # [None, 3,1,2,0, None, 1]
        # idx : left child - idx * 2, right - idx * 2 + 1
        self.arr = [None]

    # inserts a key into the priority queue
    def insert(self, key):
        # runtime O(lgn)
        # space O(1)
        self.arr.append(key)
        self.swim()

    # helper function for insert
    def swim(self):
        # parent idx: idx//2
        idx = len(self.arr) - 1
        while idx // 2 > 0 and self.arr[idx // 2] < self.arr[idx]:
            self.arr[idx], self.arr[idx // 2] = self.arr[idx // 2], self.arr[idx]
            idx = idx // 2

    # returns the largest key
    def get_max(self):
        assert not self.isEmpty()
        return self.arr[1]

    # return and remove the largest key
    def delMax(self):
        # runtime - lg(N)
        # space O(1)
        assert not self.isEmpty()
        self.arr[1], self.arr[len(self.arr) - 1] = self.arr[len(self.arr) - 1], self.arr[1]
        val = self.arr.pop()
        self.sink()
        return val

    # helper function for delete
    def sink(self):
        idx = 1
        while idx * 2 < len(self.arr):
            cur = self.arr[idx]
            left = self.arr[idx * 2]
            right = float('-inf')
            if idx * 2 + 1 < len(self.arr):
                right = self.arr[idx * 2 + 1]
            if cur >= left and cur >= right:
                return
            if left > cur:
                self.arr[idx], self.arr[idx * 2] = self.arr[idx * 2], self.arr[idx]
                idx = idx * 2
            else:
                self.arr[idx], self.arr[idx * 2 + 1] = self.arr[idx * 2 + 1], self.arr[idx]
                idx = idx * 2 + 1

    # returns a boolean indicating if the priority queue empty
    def isEmpty(self):
        return len(self.arr) == 1

    # returns the number of keys in the priority queue
    def size(self):
        return len(self.arr) - 2


def heapSort(arr):
    # sorts array by using a MaxPriorityQueue
    pq = MaxPriorityQueue()

    # O(NlgN) time
    # O(N) space
    for item in arr:
        pq.insert(item)

    idx = len(arr) - 1
    # O(NlgN) time
    # O(1) space
    while not pq.isEmpty():
        arr[idx] = pq.delMax()
        idx -= 1

    # O(NlgN) + O(NlgN) = O(2NlgN) = O(NlgN) - runtime
    # O(N) - space


if __name__ == '__main__':
    # test cases
    # arr = [6, 10, 4, 3, 2, 7, 8, 9, 1, 5, 11, 12, 4, 5, -6]
    arr = [21, 12, -1, 13, 11]
    # heapSort(arr)
    # print(arr)
    pq = MaxPriorityQueue()
    for num in arr:
        pq.insert(num)
    print(pq.arr)
    print(pq.size())
