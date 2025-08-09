"""
Key Insights
    Understanding the Problem:
        - For each day `i`, we need to find the number of days until a 
          warmer temperature occurs.
        - If there is no future day with a warmer temperature, 
          we set `answer[i] = 0`.
        - The input is an array of temperatures, and we need an efficient 
          way to process this array.

Possible Approaches:
    1. Brute Force:
        - For each day `i`, check all future days to find a warmer temperature.
        - Time Complexity: O(n²), which is not efficient for 
          large inputs (n up to 10⁵).
    2. Stack-Based Solution (Monotonic Stack):
        - Use a stack to keep track of the indices of temperatures.
        - The stack maintains a monotonically decreasing sequence of temperatures.
        - When we find a temperature higher than the one at the index on the 
          top of the stack, we can calculate the number of days between them.
        - Time Complexity: O(n), which is efficient for larger inputs.

Monotonic Stack:
    - A stack data structure where the elements are kept in monotonic order.
    - In this problem, we use a monotonically decreasing stack of temperatures.

How It Works:
    - As we iterate through the temperatures, we perform the following steps:
    1. While the current temperature is greater than the temperature at the 
       index on the top of the stack:
        - Pop the index from the stack.
        - Set `answer[index] = current_index - index`.
    2. Push the current index onto the stack.

Algorithm Intuition:
    - We maintain a stack of indices where the temperatures are decreasing.
    - When we find a warmer temperature, we resolve all previous days that were 
      waiting for a warmer temperature by popping indices from the stack.
    - This ensures that each temperature is processed at most 
      twice (once when pushed onto the stack and once when popped off).

---

Algorithm Design:
    1. Initialize:
        - Create an array `answer` of the same length as `temperatures`, initialized with zeros.
        - Initialize an empty stack to hold indices.
    2. Iterate through temperatures:
    - For each index `i` from 0 to `n-1`:
        - While the stack is not empty and `temperatures[i] > temperatures[stack[-1]]`:
            - Pop `prev_index` from the stack.
            - Calculate `answer[prev_index] = i - prev_index`.
        - Push `i` onto the stack.
    3. After Iteration:
        - Any indices left in the stack will have `answer[index] = 0` 
          (already initialized), as there are no future days with a warmer temperature.

---

Time and Space Complexity:

- Time Complexity: O(n)
  - Each index is pushed onto the stack once and popped off at most once.
  - Therefore, the total number of operations is proportional to `2n`.

- Space Complexity: O(n)
  - In the worst case, the stack may contain all indices (if the temperatures are strictly decreasing).
  - Additionally, the `answer` array uses O(n) space.

"""

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        n = len(temperatures)

        answer = [0] * n  # Initialize answer array with zeros

        # Monotonic Decreasing Stack to keep track of indices in decreasing order of temperatures
        stack = []

        for i in range(n):
            # new item should always be greater than current top item
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                answer[prev_index] = i - prev_index
            # Push current index onto the stack
            stack.append(i)

        # Any indices left in the stack have no warmer temperature in the future
        return answer

