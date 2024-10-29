"""
Key Insights  
Exponentiation by Squaring:
- A common and efficient method to compute large exponents.
- Reduces the time complexity from O(n) to O(log n) by recursively squaring the 
  base.

Handling Negative Exponents:
- A negative exponent n means we need to compute the reciprocal of x^n.
- That is, x^n = 1 / x^-n when n is negative.

Edge Cases:
- Zero Exponent (n = 0): Any non-zero number raised to the power of zero is 1.
- Zero Base (x = 0): Zero raised to any positive power is 0.
- Overflow Considerations: Ensure that we avoid integer overflow when n is 
  -2^31

Recursive vs. Iterative Implementation:
- Recursive Approach:
  - Cleaner and more intuitive implementation using recursion.
  - Be cautious of stack overflow for large n values.
  
- Iterative Approach:
  - Avoids recursion by using a loop.
  - Preferred in production code for better control over stack usage.

Approach  
We will use the Exponentiation by Squaring method, which works as follows:
- Base Case: If n == 0, return 1.
- Recursive Case:
  - If n is even:
    - pow(x, n) = pow(x * x, n // 2)
  - If n is odd:
    - pow(x, n) = x * pow(x * x, n // 2)
- This method reduces the exponent n by half at each step, achieving 
  logarithmic time complexity.

Algorithm Steps  
1. Handle Negative Exponent:
   - If n is negative, compute the reciprocal of x and make n positive.
   - Be cautious with n = -2^31, as -n would cause overflow. Use n = -(n + 1)
     and adjust accordingly.

2. Implement Exponentiation by Squaring:
   - Use a helper function to perform the recursive calculation.
   - In the recursive function:
     - Base Case: If n == 0, return 1.
     - Recursive Case:
       - Compute half = pow(x, n // 2)
       - If n is even, return half * half.
       - If n is odd, return half * half * x.

3. Iterative Version (Optional):
   - Use a loop to iteratively compute the result.
   - Initialize result = 1
   - While n > 0:
     - If n is odd, multiply result by x
     - Square x
     - Divide n by 2

4. Handle Edge Cases:
   - If x is 0, return 0 (if n > 0).
   - If n = 0, return 1 (as any number to the power 0 is 1).


Time and Space Complexity::
    Recursive Approach:
        - Time Complexity: O(log n)
            - At each recursive call, the exponent n is halved
        - Space Complexity: O(log n)
            - Due to the recursive call stack.

    Iterative Approach:
        - Time Complexity: O(log n)
            - The loop runs while n > 0, halving n each time.
        - Space Complexity: O(1)
            - Only a constant amount of space is used.

"""

class Solution:
    """ Iterative Approach"""
    def myPow(self, x: float, n: int) -> float:

        # Handle negative exponent
        negative_exponent = n < 0

        power = -n if negative_exponent else n

        result = 1.0

        current_product = x

        # Reduce power to 0
        while power > 0:
            # Odd Exponent
            if power % 2 == 1:
                result *= current_product
                power -= 1

            # Even Exponent
            else:
                current_product *= current_product
                power = power // 2

        if negative_exponent:
            return 1 / result

        return result


class Solution2:
    """ Recursive Approach"""
    def myPow(self, base: float, exponent: int) -> float:

        # If the exponent is negative, invert the base and make the exponent positive
        if exponent < 0:
            base = 1 / base
            exponent = -exponent

        def calculate_power(base: float, exponent: int) -> float:

            # Base case: any number raised to the power of 0 is 1
            if exponent == 0:
                return 1.0

            # Special case: if the base is 0, return 0 (0 raised to any power is 0)
            if base == 0:
                return 0

            # If the exponent is even, recursively calculate power with half the exponent
            if exponent % 2 == 0:
                half_power = calculate_power(base * base, exponent // 2)
                return half_power

            # If the exponent is odd, multiply the base by the result of the recursive call
            return base * calculate_power(base, exponent - 1)

        # Initiate the recursive process
        return calculate_power(base, exponent)

