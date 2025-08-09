"""
### Approach
To solve the problem, we can visualize it as a graph traversal problem. Each 
node in the graph represents the current remainder of `n` after subtracting 
some perfect square, and the edges represent the perfect square subtraction. 
Our goal is to find the shortest path from `n` to `0` using the smallest number 
of perfect square subtractions.

### Explanation of the BFS (Breadth-First Search) Approach
We use a BFS to explore all possible perfect squares that can be subtracted 
from `n` level by level. The key insight is that the first time we encounter 
`0`, the number of steps taken to reach that point is the minimum number of 
perfect square subtractions.

- **Queue**: The queue (`deque`) is used to explore each node (remainder) level 
  by level.
- **Levels**: Each level represents the number of perfect square subtractions. 
  Every time we move to the next level, we increment the count, which tracks 
  how many perfect squares were subtracted.
- **Termination**: The BFS stops when we first encounter a remainder of `0`, 
  meaning we've found the minimum number of perfect squares that sum to `n`.

### Time Complexity
- **Time Complexity**: `O(n * sqrt(n))` — For each number from `n` down to `0`, 
  we explore up to `sqrt(n)` perfect squares. This gives us a complexity of 
  `O(n * sqrt(n))`.

### Space Complexity
- **Space Complexity**: `O(n)` — We use a queue to store the remainders and 
  also a set to keep track of visited nodes, leading to a space complexity of 
  `O(n)`.

"""


from collections import deque

class Solution:
    def numSquares(self, n: int) -> int:
        """
        Finds the minimum number of perfect squares that sum up to 'n' using BFS.

        Args:
        n (int): The target number for which we need to find the minimum number of perfect square sums.

        Returns:
        int: Minimum number of perfect squares that sum to 'n'.
        """

        # Initialize a queue for BFS
        q = deque([n])
        count = 0  # Count of levels (perfect square subtractions)

        # Perform BFS
        while q:
            count += 1  # Increment the level

            # Iterate over the current level
            for _ in range(len(q)):
                curr = q.popleft()  # Get the current node (remainder)

                # Explore all perfect squares less than or equal to current remainder
                for num in range(1, int(curr**0.5) + 1):
                    rem = curr - (num * num)

                    # If remainder is zero, return the count as the minimum number of steps
                    if rem == 0:
                        return count

                    # If the remainder is still positive, add it to the queue for further exploration
                    q.append(rem)

        return count  # If no perfect squares found, return the total count (edge case)



# TESTS ------------------------------
import unittest

class TestNumSquares(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_small_numbers(self):
        self.assertEqual(self.solution.numSquares(12), 3)  # 12 = 4 + 4 + 4
        self.assertEqual(self.solution.numSquares(13), 2)  # 13 = 4 + 9

    def test_large_number(self):
        self.assertEqual(self.solution.numSquares(100), 1)  # 100 = 10^2

    def test_edge_case(self):
        self.assertEqual(self.solution.numSquares(1), 1)   # 1 = 1^2
        self.assertEqual(self.solution.numSquares(2), 2)   # 2 = 1^2 + 1^2
        self.assertEqual(self.solution.numSquares(0), 0)   # No steps needed

if __name__ == '__main__':
    unittest.main()

