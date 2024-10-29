
import heapq
from typing import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:

        counter = Counter(s)

        mh = [(-v, k) for k,v in counter.items()]
        heapq.heapify(mh)


        res = []
        prev_count, prev_char = 0, ''

        while mh or prev_count:

            if prev_count and not mh:
                return ""

            count, char = heapq.heappop(mh)

            res.append(char)
            count = -count - 1

            if prev_count:
                heapq.heappush(mh, (-prev_count, prev_char))

            prev_count, prev_char = count, char

        return ''.join(res)


