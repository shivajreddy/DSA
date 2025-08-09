"""

Example: [3, 5]

        [ 3 5 ]  <- array
          0 1    <- index

          3 8    <- prefix-array

        So for this input, the problem says that you should 
        pick index-0: 3 out of 8 times
        pick index-1: 5 out of 8 times

        1   2   3   4   5   6   7   8   <- all possible weights
        3   3   3   8   8   8   8   8   <- prefix
        0   0   0   1   1   1   1   1   <- index of the above prefix

        - As you can see, if we have a prefix array, and we know the maximum
          weight which the last item in the prefix array.
        - All the possible weights are 1..total_weight
        - Now pick a random weight out of all the possible weights
        - For this randomly picked weigth, find the first prefix that is 
          >= to the randomly picked weight

          In the above example: you could randomly pick anything in b/w 1..8
          And if you think about it, for numbers 1,2,3 your prefix is 3 because
          that is the first prefix >= 1 or 2 or 3
          Similarly for any random number picked b/w  4,5,6,7,8 the prefix would
          be 8.
          And as you can see now:
            3/8 would pick the prefix 3 which maps to idx:0
            5/8 would pick the prefix 8 which maps to idx:1

        - so ultimately, having a prefix array, and randomly picking a weight(r)
          among all the possible weights and finding the 1st prefix >= r, will
          lead result in randomly picking an index based on the indexe's weight


Step-by-Step Process:

1. Compute the Prefix Sum Array:
   - Start with the first weight: The first weight is 1.
   - Add the next weight to the cumulative sum:  
     1 + 3 = 4.
   - Prefix Sum Array:  
     The resulting prefix sum array is [1, 4].

2. Generate a Random Number:
   - Total sum of weights: The total sum of the weights is 4.
   - Generate a random integer `r` in the range [1, 4] (inclusive).
   - Possible Values of `r`:  
     `r` could be 1, 2, 3, or 4.

3. Map the Random Number to an Index Using Binary Search:
   - Goal: Find the smallest index in the prefix sum array where the 
     prefix sum is greater than or equal to `r`. This index corresponds to the
     selected weight.

4. Performing Binary Search:
   Here’s how to perform the binary search:
   - Initialize Pointers:
     - `left = 0`
     - `right = length of prefix_sum - 1 = 1`
   - Iteration 1:
     - Calculate Midpoint:  
       `mid = left + (right - left) // 2 = 0 + (1 - 0) // 2 = 0`.
     - Check Condition:  
       `prefix_sum[mid] = 1` vs. `r = 4`.
     - Since 1 < 4, move the left pointer:  
       `left = mid + 1 = 1`.
   - Iteration 2:
     - Calculate Midpoint:  
       `mid = 1 + (1 - 1) // 2 = 1`.
     - Check Condition:  
       `prefix_sum[mid] = 4` vs. `r = 4`.
     - Since 4 >= 4, move the right pointer:  
       `right = mid - 1 = 0`.
   - Termination:
     - The loop terminates when `left > right`.

5. Selected Index:
   - The final value of `left` is 1, so the selected index is 1.

6. Mapping the Random Number to the Index:
   - If `r = 4`: The binary search identifies index 1 as the correct position.
   - Interpretation:  
     Index 1 in the original weights array [1, 3] corresponds to the weight 3.

Time & Space:
Time: 
    Initialization: O(N)
    Pick-Index: O(log.N) since we binary search
Space: O(N) for the prefix array

"""

import random
import bisect

class Solution:
    def __init__(self, w):
        self.prefix_sum = []
        current_sum = 0
        for weight in w:
            current_sum += weight
            self.prefix_sum.append(current_sum)
        self.total = current_sum

    def pickIndex(self):
        r = random.randint(1, self.total)
        # bisect.bisect_left returns the leftmost place where r can be inserted
        index = bisect.bisect_left(self.prefix_sum, r)
        return index


