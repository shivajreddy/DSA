"""
### Key Insights:

#### Monotonic Stack:
- A monotonic stack is an efficient way to solve problems related to "next 
  greater element" by keeping track of indices where the next greater element 
  hasn’t been found yet.
- The stack will store indices in a way that the elements corresponding to 
  these indices are in descending order.
- When we encounter an element that is greater than the element corresponding 
  to the index at the top of the stack, we know we’ve found the "next greater" 
  for that element, and we pop it from the stack.

#### Circular Array:
- We can simulate the circular nature of the array by iterating twice over the 
  array. This ensures that for any element, we consider potential greater 
  elements that might appear later, even if they wrap around.

### Plan:
1. Iterate through the array twice to simulate the circular behavior.
2. Use a stack to store indices of the elements that we have not yet found a 
   "next greater" element for.
3. Pop from the stack when we find an element that is greater than the element 
   at the top of the stack, and update the result for that index.
4. Return the result array, which contains the next greater elements for each 
   index.

### Time Complexity:
- `O(N)`: Each element is pushed and popped from the stack at most once, 
  leading to a linear time complexity.
- `O(N)` space is used for the stack and result array.

### Explanation:

#### Result Array Initialization:
- We initialize a result array with `-1` values. This indicates that initially, 
  we assume no "next greater element" exists for any position.

#### Circular Array Simulation:
- We loop through the array twice by iterating over `range(2 * n)`. This allows 
  us to simulate the circular behavior. For each iteration, the index `idx` is 
  calculated using `i % n`.

#### Monotonic Stack:
- For each index, we check if the current element (`nums[idx]`) is greater than 
  the element at the index stored at the top of the stack (`nums[stack[-1]]`). 
  If it is, we pop from the stack and assign the current element as the next 
  greater element for that popped index.
- This ensures that we efficiently process each element and find the "next 
  greater element" in a single pass.

#### Stack Storage:
- We store indices in the stack, not the elements themselves. This allows us to 
  easily update the result array and handle wraparounds.

#### First Pass Only Stack Push:
- We only push indices onto the stack during the first pass (i.e., when `i < 
  n`). During the second pass, we’re only checking to resolve the "next 
  greater" elements for indices that were not resolved in the first pass.

### Example Walkthrough:
nums = [1, 2, 1]
### First iteration (i = 0):
- **Current element**: `nums[0] = 1`
- Stack is empty, so we push index `0` onto the stack.

### Second iteration (i = 1):
- **Current element**: `nums[1] = 2`
- `nums[1]` is greater than `nums[0]` (top of the stack), so we pop `0` and set 
  `result[0] = 2`.
- Push index `1` onto the stack.

### Third iteration (i = 2):
- **Current element**: `nums[2] = 1`
- `nums[2]` is not greater than `nums[1]` (top of the stack), so we push index 
  `2` onto the stack.

### Fourth iteration (i = 3, idx = 0) (Simulating circular array):
- **Current element**: `nums[0] = 1`
- Stack remains unchanged since `nums[0]` is not greater than `nums[2]`.

### Fifth iteration (i = 4, idx = 1):
- **Current element**: `nums[1] = 2`
- `nums[1]` is greater than `nums[2]`, so we pop `2` from the stack and set 
  `result[2] = 2`.

### Sixth iteration (i = 5, idx = 2):
- Stack remains unchanged since `nums[2]` is not greater than `nums[1]`.

The final result array is `[2, -1, 2]`.

### Edge Cases:
- **Single Element**: The next greater element for a single element is `-1` 
  since there's no other element.
- **All Elements Equal**: If all elements are equal, the result will be `-1` 
  for all positions since no greater element exists.
- **Decreasing Array**: For an array in strictly decreasing order, all 
  elements' next greater element will wrap around, and only the largest element 
  will have `-1`.

### Time and Space Complexity:
- **Time Complexity**: `O(N)` because we iterate over the array twice and each 
  element is pushed and popped from the stack once.
- **Space Complexity**: `O(N)` due to the stack and result array.

"""




from typing import List



class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n  # Initialize the result with -1
        stack = []  # Stack to hold indices of the elements

        # Loop over the array twice to simulate the circular nature
        for i in range(2 * n):
            # Index in the circular array
            idx = i % n

            # While stack is not empty and the current element is greater
            # than the element at the index stored at the top of the stack
            while stack and nums[stack[-1]] < nums[idx]:
                top_idx = stack.pop()  # Pop the top index
                result[top_idx] = nums[idx]  # Assign the next greater element

            # We push the index to the stack only if we're in the first pass
            # (i.e., i < n) because after that we are just simulating the circular behavior.
            if i < n:
                stack.append(idx)

        return result

