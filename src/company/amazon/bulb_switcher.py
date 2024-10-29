"""
Key Insights:

Toggle Frequency and Divisors:
- A bulb `k` is toggled in every round that is a divisor of `k`. 
For example, bulb 6 is toggled in rounds 1, 2, 3, and 6 because these numbers divide 6.

Number of Toggles Determines Final State:
- If a bulb is toggled an odd number of times, it ends up on.
- If toggled an even number of times, it remains off.

Perfect Squares Have Odd Number of Divisors:
- Only perfect squares have an odd number of divisors. For instance, 9 has divisors 1, 3, 9 (three divisors), whereas 8 has divisors 1, 2, 4, 8 (four divisors).
- Therefore, bulbs positioned at perfect square numbers will be on after `n` rounds.

Mathematical Implication:
- The number of bulbs that remain on is equal to the count of perfect squares less than or equal to `n`.
- This count is essentially the integer part of the square root of `n`.

Plan

Mathematical Computation:
- Compute the integer square root of `n`. This gives the count of perfect squares ≤ `n`.

Edge Case Handling:
- Ensure that `n` is within the valid range (1 ≤ `n` ≤ 10^9) as per problem constraints.
- Handle cases where `n` is 0 or 1 appropriately.

Implementation Considerations:
- Utilize efficient mathematical functions to compute the square root.
- Ensure that the solution runs in constant time (O(1)), as the computation is straightforward.

Time and Space Complexity

Time Complexity: O(1)
- The solution involves a simple mathematical computation that does not depend on the size of `n`.

Space Complexity: O(1)
- Only a few variables are used, regardless of the input size.
"""

import math

class Solution:
    def bulbSwitch(self, n: int) -> int:
        """
        Determines the number of bulbs that are on after n rounds of toggling.

        Args:
        n (int): The number of bulbs and the number of rounds.

        Returns:
        int: The count of bulbs that are on after n rounds.
        """
        # Edge Case: If n is 0, no bulbs are on
        if n <= 0:
            return 0

        # Compute the integer square root of n
        # math.isqrt is available from Python 3.8 onwards
        # For compatibility, we use int(math.sqrt(n)) which truncates towards zero
        return int(math.sqrt(n))

