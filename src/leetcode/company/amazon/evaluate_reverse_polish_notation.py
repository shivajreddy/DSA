"""
Problem: Evaluate Reverse Polish Notation (RPN)


Given a list of tokens representing an arithmetic expression in Reverse Polish Notation,
evaluate the expression and return the result.


Valid operators are '+', '-', '*', and '/'. Each operand may be an integer or another expression.
Division between two integers should truncate toward zero.


Constraints:
- The given RPN expression is always valid.
- Division by zero will not be encountered.


Approach:
- Use a stack to store operands.
- Iterate through each token:
 - If the token is an operator, pop the top two operands from the stack,
   perform the operation, and push the result back onto the stack.
 - If the token is a number, convert it to an integer and push onto the stack.
- After processing all tokens, the result will be the only element left in the stack.


Time Complexity: O(n), where n is the number of tokens.
Space Complexity: O(n), due to the stack used for computation.


Edge Cases:
- Negative Numbers: Correctly handle negative integers in the tokens.
- Division: Ensure that division between two integers truncates toward zero.


Future Improvements:
- Add error handling for invalid tokens or insufficient operands.
- Extend support for additional operators (e.g., exponentiation, modulus).
- Optimize space by reusing the input list for the stack if mutations are allowed.


### Time and Space Complexity:


- **Time Complexity**: `O(n)`, where `n` is the number of tokens, since we process
 each token exactly once.


- **Space Complexity**: `O(n)`, due to the stack used to store operands during
 computation.


### Edge Cases Handled:


- **Negative Numbers**: By converting tokens to integers using `int(token)`, the
 code correctly handles negative numbers.


- **Division Truncation**: Division results are truncated towards zero using
 `int(a / b)` to meet the problem's requirements.


### Future Improvements:


- **Error Handling**: Implement additional checks and exceptions for invalid inputs
 or insufficient operands.


- **Additional Operators**: Extend the solution to handle more complex operations
 like exponentiation or modulus.


- **Space Optimization**: If mutations are allowed, reuse the input tokens list to
 save space instead of using an extra stack.


"""


from typing import List


class Solution:
   def operation(self, a: int, b: int, operation: str) -> int:
       """
       Perform the arithmetic operation on two operands.


       Args:
           a (int): The first operand.
           b (int): The second operand.
           operation (str): The operator ('+', '-', '*', '/').


       Returns:
           int: The result of the operation.


       Raises:
           ValueError: If an invalid operation is provided.
       """
       if operation == '+':
           return a + b
       elif operation == '-':
           return a - b
       elif operation == '*':
           return a * b
       elif operation == '/':
           # Division should truncate toward zero
           return int(a / b)
       else:
           raise ValueError(f"Invalid operation: {operation}")


   def evalRPN(self, tokens: List[str]) -> int:
       """
       Evaluate the value of an arithmetic expression in Reverse Polish Notation.


       Args:
           tokens (List[str]): The list of tokens representing the RPN expression.


       Returns:
           int: The result of evaluating the expression.
       """
       stack = []
       for token in tokens:
           if token in '+-*/':
               # Pop the top two operands from the stack
               b = stack.pop()
               a = stack.pop()
               # Perform the operation and push the result back onto the stack
               res = self.operation(a, b, token)
               stack.append(res)
           else:
               # Convert the token to integer and push onto the stack
               # Handles negative numbers as well
               stack.append(int(token))
       # The final result will be the only element left in the stack
       return stack[0]

