from typing import List

class SegmentTree_Shiva:
    def __init__(self, n):
        size = 1
        while size <= n:
            size *= 2   # or size <<= 1
        tree = [0] * (2 * size)
        self.size, self.tree= size, tree

    def query_range(self, l, r):
        l += self.size - 1
        r += self.size - 1
        
        res = 0
        while l <= r:
            if l % 2 == 1:
                res += self.tree[l]
                l += 1
            if r % 2 == 0:
                res += self.tree[r]
                r -= 1
            l //= 2
            r //= 2

    def update_tree(self):
        pass


class SegmentTree:
    def __init__(self, n):
        self.size = 1
        while self.size <= n:
            self.size *= 2
        self.tree = [0] * (2 * self.size)

    def query_range(self, l, r):
        l += self.size - 1
        r += self.size - 1
        res = 0
        while l <= r:
            if l % 2 == 1:
                res += self.tree[l]
                l += 1
            if r % 2 == 0:
                res += self.tree[r]
                r -= 1
            # l >>= 1
            # r >>= 1
            l //= 2
            r //= 2
        return res

    def update_tree(self, idx, value):
        idx += self.size - 1
        self.tree[idx] += value
        while idx > 1:
            # idx >>= 1
            idx //= 2
            self.tree[idx] = self.tree[2 * idx] + self.tree[2 * idx + 1]


class Solution:
    def numTeams(self, ratings: List[int]) -> int:
        # Coordinate compression
        sorted_unique = sorted(set(ratings))
        rating_to_index = {rating: idx+1 for idx, rating in enumerate(sorted_unique)}

        # Initialize left and right trees
        max_index = len(sorted_unique)
        left_tree = SegmentTree(max_index)
        right_tree = SegmentTree(max_index)

        # Initialize right_tree with all ratings
        for rating in ratings:
            idx = rating_to_index[rating]
            right_tree.update_tree(idx, 1)

        total = 0
        for rating in ratings:
            idx = rating_to_index[rating]

            # Remove current rating from right_tree
            right_tree.update_tree(idx, -1)

            # Query left_tree
            left_smaller = left_tree.query_range(1, idx - 1) if idx > 1 else 0
            left_greater = left_tree.query_range(idx + 1, max_index) if idx < max_index else 0

            # Query right_tree
            right_smaller = right_tree.query_range(1, idx - 1) if idx > 1 else 0
            right_greater = right_tree.query_range(idx + 1, max_index) if idx < max_index else 0

            # Update total
            total += ( (left_smaller * right_greater) + (left_greater * right_smaller) )

            # Update left_tree
            left_tree.update_tree(idx, 1)
        
        return total
