class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:

        hm = {}

        def rec(i):

            # base case
            if i == len(days):
                return 0
            if i in hm:
                return hm[i]

            hm[i] = float("inf")
            for day, cost in zip([1, 7, 30], costs):  # loop with different day-lengths
                j = i  # # max_index for that day
                while j < len(days) and cost + days[i] > days[j]:
                    j += 1
                hm[i] = min(hm[i], cost + rec(j))
            return hm[i]

        return rec(0)
