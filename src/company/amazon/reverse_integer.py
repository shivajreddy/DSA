"""
### Key Considerations:
- A signed 32-bit integer can range from `-2^31` to `2^31 - 1`, or 
  `-2147483648` to `2147483647`.
- Reversing a number can cause overflow if the result exceeds the range of a 
  signed 32-bit integer.
- The result should preserve the sign (negative or positive) of the input 
  number.

### Plan:
- **Extract digits**: We can reverse the integer by extracting the digits one 
  at a time from the original number.
- **Handle overflow**: After each digit extraction and reversal, check if the 
  reversed number exceeds the 32-bit signed integer range.
- **Use modulo and division**: We use modulo (`%`) to extract the last digit of 
  the number and integer division (`//`) to remove the last digit from the 
  number.

### Time Complexity:
- **Time**: `O(log(x))`: The time complexity is proportional to the number of 
  digits in the integer, which is logarithmic with respect to the value of the 
  integer.
- **Space Complexity**: `O(1)`: We are using only a few extra variables, so the 
  space complexity is constant.

### Explanation:
- **Sign handling**: We store the sign of `x` and work with the absolute value 
  of `x` to simplify the reversal logic.
- **Main loop**: We extract the last digit of `x` using `x % 10` and append it 
  to the reversed number. Then, we divide `x` by 10 to remove the last digit.
- **Overflow check**: Before updating the reversed number, we check if 
  multiplying `result` by 10 and adding the next digit would cause it to 
  overflow. This is done by ensuring that `result` is not greater than 
  `(INT_MAX - digit) // 10` (i.e., the threshold before overflow).
- **Final return**: After reversing all the digits, we multiply the result by 
  the original sign and return it. If overflow occurs, we return `0`.

### Step-by-Step Example:
#### Initial: 
- `x = 123`, `result = 0`, `sign = 1`

#### First iteration:
- Extract last digit: `digit = 123 % 10 = 3`
- Update result: `result = 0 * 10 + 3 = 3`
- Update `x`: `x = 123 // 10 = 12`

#### Second iteration:
- Extract last digit: `digit = 12 % 10 = 2`
- Update result: `result = 3 * 10 + 2 = 32`
- Update `x`: `x = 12 // 10 = 1`

#### Third iteration:
- Extract last digit: `digit = 1 % 10 = 1`
- Update result: `result = 32 * 10 + 1 = 321`
- Update `x`: `x = 1 // 10 = 0`

#### Final result:
- `result = 321`, sign is positive, so return `321`.

### Edge Cases:
- **Overflow**: 
  - If reversing the number would cause it to exceed the 32-bit integer range 
    (`[-2^31, 2^31-1]`), the function returns `0`. This is handled during the 
    overflow check inside the loop.
  - For example, if `x = 1534236469` (which would overflow), the reversed 
    result would exceed `2147483647`, so the function returns `0`.

- **Single-digit numbers**: 
  - If `x` has only one digit (e.g., `5` or `-7`), the reverse is the same as 
    the original number.

- **Zero**: 
  - If `x = 0`, the result is `0`.

### Optimization Notes:
- The approach avoids unnecessary string manipulation or extra data 
  structures, ensuring `O(1)` space complexity.
- The overflow check ensures the solution handles all edge cases efficiently, 
  including large integers and negative numbers.
- This approach is optimal with `O(log(x))` time complexity, given that the 
  number of digits grows logarithmically with the size of the integer. It is 
  also concise and handles edge cases in a clear and efficient manner.

"""



class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1     # 2147483647
        INT_MIN = -2**31        # -2147483648

        sign = -1 if x < 0 else 1
        x = abs(x)  # Work with the absolute value

        result = 0

        while x != 0:
            digit = x % 10      # Get the last digit
            x //= 10            # Remove the last digit from x

            # Check for overflow before updating the result
            if result > (INT_MAX - digit) // 10:
                return 0  # Return 0 if it would overflow

            # Append the digit to the reversed number
            result = result * 10 + digit

        return sign * result

