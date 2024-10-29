"""
Key Insights  
Dynamic Programming (DP) with Memoization:  
    - Approach: Utilize a top-down DP strategy where the solution is built by recursively determining the optimal placement
      of books starting from each index.  
    - Memoization: Essential for storing intermediate results (`memo[i]`) to avoid redundant computations,
      thereby ensuring efficiency.  


Optimal Substructure:  
    - Property: The problem exhibits an optimal substructure, meaning the optimal solution for placing books starting
      from index `i` can be constructed from the optimal solutions of placing books from subsequent indices.  
    - Implication: By solving smaller subproblems (placing books from `j + 1` onward), we can build up the solution for
      the current state (`i`).  


State Definition:  
    - Definition: `DP[i]` represents the minimum total height of the bookcase when placing books starting from
      index `i` to the end.  
    - Objective: Compute `DP[0]`, which signifies the minimum total height for placing all books.  


Recurrence Relation:  
- Process:  
  - For each starting index `i`, consider placing books from `i` to `j` on the current shelf.  
  - Ensure that the cumulative thickness (`current_thickness`) of books from `i` to `j` does not exceed `shelf_width`.  
  - Determine the maximum height (`current_max_height`) among these books.  
  - The total height for this placement is `current_max_height + DP[j + 1]`, where `DP[j + 1]` is the minimum height
    for the remaining books.  
- Update Rule: Set `DP[i]` as the minimum of all possible `total_height` values obtained by varying `j`.  


Time and Space Efficiency:  
    - Time Complexity: O(n²)  
    - For each book index `i`, the algorithm may iterate through all subsequent books `j`,
      leading to a quadratic time complexity.  


    - Space Complexity: O(n)  
    - The memoization cache (`memo`) stores a result for each index `i`, requiring linear space.  
    - The recursion stack also consumes linear space in the worst case.  
---


Detailed Plan  


Initialization:  
- Determine the total number of books `n`.  
- Initialize an empty dictionary `memo` to store the minimum total height for each starting index `i`.  


Define the Recursive Function (dfs):  
- Purpose: Compute the minimum total height for placing books starting from index `i` to the end.  


- Base Case:  
  - If `i == n`, return 0 since there are no more books to place.  


- Memoization Check:  
  - If the result for index `i` is already computed (`i` in `memo`), return the cached value to avoid redundant computations.  


- Recursive Case:  
  - Initialize `min_total_height` to infinity to keep track of the minimum height found.  
  - Initialize `current_thickness` and `current_max_height` to 0.  
  - Iterate over the books starting from index `i` to `n - 1`:  
    - Add Thickness:  
      - Add the thickness of book `j` to `current_thickness`.  
      - If `current_thickness` exceeds `shelf_width`, break the loop as no more books can fit on the current shelf.  
    - Update Maximum Height:  
      - Update `current_max_height` to be the maximum of itself and the height of book `j`.  
    - Recursive Call:  
      - Recursively compute the minimum total height for the remaining books starting from `j + 1` by calling `dfs(j + 1)`.  
    - Update Minimum Total Height:  
      - Calculate `total_height` as the sum of `current_max_height` and the result of the recursive call.  
      - Update `min_total_height` with the minimum value between the current `min_total_height` and `total_height`.  


- Cache the Result:  
  - Store the computed `min_total_height` in `memo[i]` to cache the result for the current index.  


- Return the Result:  
  - Return `min_total_height` as the minimum total height for placing books starting from index `i`.  


Final Computation:  
- Invoke `dfs(0)` to compute the minimum total height for placing all books starting from the first book.  
- Return the result of `dfs(0)` as the final answer.  


---


Time and Space Complexity  


- Time Complexity: O(n²)  
  - The algorithm considers each possible starting index `i` and iterates through all possible ending indices `j` for placing books on the current shelf. This nested iteration leads to a quadratic time complexity.  
- Space Complexity: O(n)  
  - The memoization dictionary `memo` stores a result for each index `i`, requiring linear space.  
  - Additionally, the recursion stack may grow linearly with the number of books in the worst case.  


Feasibility:  
- Given the constraint `n <= 1000`, the O(n²) time complexity is acceptable and ensures that the solution runs efficiently within reasonable time limits.
"""


from typing import List
from functools import lru_cache


class SolutionTopDown:
# class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        """
        Determines the minimum total height of the bookcase after placing all books.

        Args:
        books (List[List[int]]): A list where each element is [thickness, height] of a book.
        shelf_width (int): The maximum width of each shelf.

        Returns:
        int: The minimum total height of the bookcase.
        """
        n = len(books)


        memo = {}

        def dfs(i: int) -> int:
            """
            Recursively computes the minimum total height starting from book i.

            Args:
            i (int): The current book index.

            Returns:
            int: The minimum total height from book i to the end.
            """
            if i == n:
                return 0  # No more books to place

            if i in memo:
                return memo[i]  # return cached result

            min_total_height = float('inf')
            current_thickness = 0
            current_max_height = 0

            # Try placing books from i to j on the current shelf
            for j in range(i, n):
                current_thickness += books[j][0]
                if current_thickness > shelf_width:
                    break  # Cannot place more books on this shelf
                current_max_height = max(current_max_height, books[j][1])
                # Recursively place the remaining books
                total_height = current_max_height + dfs(j + 1)
                min_total_height = min(min_total_height, total_height)

            memo[i] = min_total_height  # Cache the result for the current index
            return min_total_height

        return dfs(0)




"""
Key Insights


Dynamic Programming (DP) Approach:


- State Definition: Let `DP[i]` represent the minimum total height for placing the first `i` books.
- State Transition: To compute `DP[i]`, consider all possible placements of the last few books on the current shelf without exceeding `shelf_width`. For each possible placement, update `DP[i]` based on the optimal substructure.


Optimal Substructure:
- The problem exhibits an optimal substructure property, meaning the optimal solution can be constructed from optimal solutions of its subproblems. This makes it suitable for DP.


Avoiding Redundant Calculations:
- By iterating backwards and keeping track of cumulative thickness and maximum height, we can efficiently compute `DP[i]` without redundant computations.


Time and Space Efficiency:
- The DP approach ensures that each state `DP[i]` is computed only once, leading to an overall time complexity of O(n²), which is acceptable given the constraints (n <= 1000).
- Space complexity is O(n), as we only need to store the DP array.


---


Detailed Plan


1. Initialize the DP Array:
   - Create a `DP` array of size `n + 1`, where `n` is the number of books.
   - Set `DP[0] = 0` since no books require zero height.


2. Iterate Through Each Book:
   - For each book `i` (1-based indexing), determine the minimum total height by considering all possible placements of the last few books on the current shelf.
   - Initialize variables to keep track of cumulative thickness (`thickness_sum`) and the maximum height (`max_height`) for the current shelf.


3. Backward Iteration for Shelf Placement:
   - For each book `i`, iterate backwards from book `i` to book `1` to explore all possible numbers of books that can fit on the current shelf.
   - Update `thickness_sum` and `max_height` accordingly.
   - If adding the current book exceeds `shelf_width`, break the loop as further books will only increase the thickness.
   - Update `DP[i]` with the minimum height found.


4. Final Result:
   - After filling the DP array, `DP[n]` will contain the minimum total height of the bookcase.


---


Time and Space Complexity


- Time Complexity: O(n²)
  - For each book `i`, we may iterate through all previous books `j`, leading to a quadratic time complexity.


- Space Complexity: O(n)
  - We use a DP array of size `n + 1` to store intermediate results.


Given the problem constraints (`n <= 1000`), this approach is efficient and feasible.
"""




from typing import List


# class SolutionBottomUp:
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        """
        Determines the minimum possible height of the bookcase after placing all books.


        Args:
        books (List[List[int]]): A list where each element is [thickness, height] of a book.
        shelf_width (int): The maximum width of each shelf.


        Returns:
        int: The minimum total height of the bookcase.
        """
        n = len(books)
        # Initialize DP array where DP[i] represents the minimum height for the first i books
        DP = [0] + [float('inf')] * n


        for i in range(1, n + 1):
            thickness_sum = 0
            max_height = 0
            # Try to place as many books as possible on the current shelf, starting from book i and going backwards
            for j in range(i, 0, -1):
                thickness_sum += books[j - 1][0]
                if thickness_sum > shelf_width:
                    break  # Cannot place more books on this shelf
                max_height = max(max_height, books[j - 1][1])
                # Update DP[i] with the minimum height found
                DP[i] = min(DP[i], DP[j - 1] + max_height)

        return DP[n]


