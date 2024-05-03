from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # multiply all stone weights with -1, cuz using minheap
        stones = [-stone for stone in stones]

        # create a min heap
        heapq.heapify(stones)

        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            if x != y:
                heapq.heappush(stones, x - y)

        return 0 if not stones else -heapq.heappop(stones)
