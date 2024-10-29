"""
Key Insights:

Backtracking with Duplicate Handling:
	- Since each candidate can be used only once, we need to ensure that we don't
	  reuse the same element in a combination.
	- The candidates array may contain duplicates, so we need a strategy to avoid
	  generating duplicate combinations.

Sorting and Skipping Duplicates:
	- Sorting the candidates array allows us to identify and skip duplicates
	  easily.
	- When we encounter consecutive duplicate elements, we can skip them during
	  iteration to avoid duplicate combinations.

Controlled Recursion:
	- We need to carefully manage the indices during recursion to ensure we don't
	  include the same element multiple times or miss potential combinations.

Plan:

	Sort the Candidates:
		- Sorting helps in identifying duplicates and allows for efficient skipping
		  of duplicate elements.

	Backtracking Function:
		- Create a recursive function that takes the remaining target sum, the
		  current combination, and the starting index.
		- At each recursive call, iterate over the candidates starting from the
		  start_index.

	Decision Making:
		- For each candidate, decide whether to include it in the current
		  combination.
		- Since each number can be used only once, we move to the next index in the
		  recursive call.

	Skip Duplicates:
		- If a candidate is the same as the one before it (and we're at the same
		  recursive depth), we skip it to prevent duplicate combinations.

	Base Cases:
		- If the remaining target sum is zero, we've found a valid combination;
		  add it to the result.
		- If the remaining target sum becomes negative or we've exhausted all
		  candidates, backtrack.

	Result Collection:
		- Collect all valid combinations in a list to be returned at the end.

Time and Space Complexity:
	Time Complexity: O(2^N)
    - where N is the number of candidates. This represents
	  the number of possible combinations. However, due to pruning and skipping
	  duplicates, the actual time is less than O(2^N).

	Space Complexity: O(N)
    - accounting for the recursion stack and the space
	needed to store the current combination.
"""

from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Sort the candidates to help with duplicate skipping
        candidates.sort()
        result = []

        def backtrack(remaining, combination, start_index):
            if remaining == 0:
                # Found a valid combination
                result.append(list(combination))
                return
            elif remaining < 0:
                # Exceeded the sum, stop exploring this path
                return

            previous = -1  # Initialize previous number to an invalid number
            for i in range(start_index, len(candidates)):
                current_candidate = candidates[i]

                # Skip duplicates at the same recursive depth
                if current_candidate == previous:
                    continue
                if current_candidate > remaining:
                    # Further candidates will be larger (since array is sorted)
                    break
                # Include the current candidate
                combination.append(current_candidate)
                # Move to the next index since each number can be used only once
                backtrack(remaining - current_candidate, combination, i + 1)
                # Backtrack: Remove the last added candidate
                combination.pop()
                # Set previous to current to check for duplicates in the next iteration
                previous = current_candidate

        # Start the backtracking with an empty combination
        backtrack(target, [], 0)
        return result

"""
Explanation:

Sorting:
	- We sort candidates to make it easier to skip duplicates and to optimize
	  the search by allowing early termination when the remaining target becomes
	  negative.

Backtracking Function (backtrack):
	Parameters:
		remaining: The remaining sum needed to reach the target.
		combination: The current combination of candidates being explored.
		start_index: The index in candidates from which to consider adding new
		candidates.

	Base Cases:
		- If remaining == 0, we have found a valid combination; we add a deep
		  copy of combination to result.
		- If remaining < 0, the current combination exceeds the target; we
		  backtrack.

	Recursive Case:
		- We iterate over candidates starting from start_index.

	Skip Duplicates:
		- We use a previous variable to keep track of the candidate at the
		  previous iteration.
		- If the current candidate is the same as previous, we skip it to prevent
		  duplicate combinations at the same recursive level.

	Early Termination:
		- If current_candidate > remaining, we break the loop since further
		  candidates will also be larger.

	Include the Candidate:
		- We add the current candidate to combination.
		- We recursively call backtrack with the updated remaining and i + 1 as
		  the new start_index because each candidate can be used only once.

	Backtrack:
		- After exploring the path including the current candidate, we remove it
		  from combination to backtrack and explore other possibilities.

	Update previous:
		- We set previous to current_candidate to help skip duplicates in the next
		  iteration.


Example Walkthrough:

Example 1:

candidates = [10,1,2,7,6,1,5]  
target = 8  

Sorted Candidates:  
[1, 1, 2, 5, 6, 7, 10]  

Process:

First Level (start_index = 0):  
	previous = -1  
	i = 0, current_candidate = 1  
	remaining = 8 - 1 = 7  
	combination = [1]  

Second Level (start_index = 1):  
	previous = -1  
	i = 1, current_candidate = 1 (duplicate at this level)  
	Include:  
	remaining = 7 - 1 = 6  
	combination = [1, 1]  

Third Level (start_index = 2):  
	Continue exploring...  
	Backtrack: Remove 1 from combination  
	previous = 1  
	i = 2, current_candidate = 2  
	Include:  
	remaining = 7 - 2 = 5  
	combination = [1, 2]  

Third Level (start_index = 3):  
	Continue exploring...  
	Backtrack: Remove 2 from combination  
	previous = 2  
	...  
	Backtrack: Remove 1 from combination  
	previous = 1  

Continue Exploring Other Candidates:  
	Skip duplicates where necessary.  
	Collect valid combinations when remaining == 0:  
	[1, 1, 6]  
	[1, 2, 5]  
	[1, 7]  
	[2, 6]  

Final Result:  
[[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]  

Example 2:

candidates = [2,5,2,1,2]  
target = 5  

Sorted Candidates:  
[1, 2, 2, 2, 5]  

Final Result:  
[[1, 2, 2], [5]]  

Edge Cases and Considerations:

Duplicates in Candidates:  
	The candidates array may contain duplicates. By sorting and skipping duplicates 
    at the same recursive depth, we avoid generating duplicate combinations.  

Each Number Used Once:  
	We ensure that each number is used at most once in a combination by incrementing
    the start_index in recursive calls.  

Empty Candidates List:  
	If candidates is empty, the result will be an empty list, as there are no
    candidates to form any combination.  

Target Value Zero:  
	If the target is zero, the only valid combination is an empty list.
    Since the problem specifies positive integers and expects combinations of
    positive numbers, we return an empty list.
"""
