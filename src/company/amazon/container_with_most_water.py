"""
### Key Insights:
The area of water that can be held between two lines is determined by the 
minimum height of the two lines and the distance between them. Mathematically:

`area = min(height[left], height[right]) × (right - left)`

A brute-force approach would be to check all pairs of lines and compute the 
area, but that would lead to `O(N^2)` time complexity, which is inefficient for 
large inputs.

### Optimized Approach: Two-Pointer Technique
To achieve an optimal solution, we can use a two-pointer approach, where:

- We initialize two pointers, left at the beginning of the array and right at 
  the end.
- At each step, calculate the area between the lines at `left` and `right`.
- Move the pointer pointing to the shorter line inward because the height of 
  the container is limited by the shorter line, and moving it might find a 
  taller line that could result in a larger area.
- Continue this until the two pointers meet.

#### This approach works because:
By moving the shorter line inward, we maximize the potential for a larger area, 
as increasing the shorter height is our best bet to find a larger container.

### Time Complexity:
- **Time**: `O(N)`, where `N` is the number of elements in the array. We 
  traverse the array once with the two-pointer approach.
- **Space**: `O(1)` because we use a constant amount of extra space.

### Explanation:
- **Two-pointer initialization**: The left pointer starts at the beginning of 
  the array, and the right pointer starts at the end.
- **Area Calculation**: At each step, we calculate the area formed between the 
  two pointers using the formula `min(height[left], height[right]) * (right - 
  left)`.
- **Pointer Movement**:
  - If the height at `left` is less than the height at `right`, we move the 
    left pointer inward (`left += 1`) because the container height is limited 
    by the shorter line.
  - If the height at `right` is less than or equal to the height at `left`, we 
    move the right pointer inward (`right -= 1`).
- **Max Area Update**: At each step, we update `max_area` if the current area 
  is larger than the previously recorded max area.
- **Termination**: The loop continues until the two pointers meet. At this 
  point, we have checked all possible pairs, and the `max_area` will hold the 
  result.

### Step-by-step:

- **Initial**: `left = 0`, `right = 8`, `max_area = 0`.
  - Calculate area: `min(1, 7) * (8 - 0) = 1 * 8 = 8`.
  - Update `max_area = 8`.
  - Move left since `height[left] < height[right]`, so `left = 1`.

- **Next**: `left = 1`, `right = 8`, `max_area = 8`.
  - Calculate area: `min(8, 7) * (8 - 1) = 7 * 7 = 49`.
  - Update `max_area = 49`.
  - Move right since `height[right] <= height[left]`, so `right = 7`.

- **Next**: `left = 1`, `right = 7`, `max_area = 49`.
  - Calculate area: `min(8, 3) * (7 - 1) = 3 * 6 = 18`.
  - `max_area` remains 49.
  - Move right to 6.

- **Next**: `left = 1`, `right = 6`, `max_area = 49`.
  - Calculate area: `min(8, 8) * (6 - 1) = 8 * 5 = 40`.
  - `max_area` remains 49.
  - Move right to 5.

- Continue this process until the pointers meet. The largest area found is 49.

### Edge Cases:
- **Minimal input**: If the array has less than two elements, the container 
  cannot exist, and we should return `0`.
- **Uniform height**: If all elements are the same, the largest container is 
  formed by the two furthest points.
- **Descending or ascending heights**: The two-pointer approach still works, as 
  it efficiently skips unnecessary checks.

### Optimization Notes:
- This solution is optimal with `O(N)` time complexity, which is necessary for 
  handling large inputs efficiently.
- By using the two-pointer technique, we avoid the inefficiency of the 
  brute-force approach, which would require checking every pair of lines.

"""

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            # Calculate the current area
            current_area = min(height[left], height[right]) * (right - left)
            # Update max_area if the current area is larger
            max_area = max(max_area, current_area)

            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

