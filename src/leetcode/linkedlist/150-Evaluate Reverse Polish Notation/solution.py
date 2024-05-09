"""
# 150 - Evaluate Reverse Polish Notation
[LeetCode](https://leetcode.com/problems/evaluate-reverse-polish-notation/)

TimeStamps:
1. Understand the Problem: 00:00 - 00:00 (00 MIN)
2. Design&Verify Solution: 00:00 - 00:00 (00 MIN)
3. Code & Pass Test Cases: 00:00 - 00:00 (00 MIN)
"""


'''
Assumptions:
  - valid revese polish notation
  - division by 0 doesn't occur
  - / -> floor division
  - does not lead with an operator
  - division trucates to zero
  - could be no operators


Test Cases:

IN : -200
OUT: -200

IN : 2 0 *
OUT: 0

IN : 2 1 + 3 *
OUT: 9

IN : 10 6 9 3 + -11 * / * 17 + 5 +
OUT: ( (10 * (6 / ((9 + 3) * -11))) + 17 ) + 5

IN : 10 6 9 3 + -11 * / *
OUT: 10 * (6 / ((9 + 3) * -11)))


IN : 2 + (3 * 5)
IN : 2 3 5 * +
     - -----
OUT: 17

IN : (2 * 5) + 3
IN :  2 5 * 3 +
      ----- -
OUT: 13

IN : (2*5) + (3*5)
IN :  2 5 * 3 5 * +
      ----- -----
OUT: 25


9 + 3
9 3 +

9 + 3  * -11
9 3 +  -11 *

6 / ( (9+3) * -11 )
6 9 3 +  -11 * /

10 * (  6 / ( (9+3) * -11 )  )
10 6 9 3 +  -11 * / *

lhs xx rhs
lhs (lhs rhs xx) xx


IN : [ "-2" ]
OUT: -2


IN : x y operation
OUT: a

IN : [ "1", "2" , "/" ]
OUT: 0

IN : [ "-1", "2" , "/" ]
OUT: 0


1 / 2 = 0.5
22/7 = 3.14______

3 // 2 = 1
-6 // 122 = -1 -> wrong

-6 / 122 = int(-0.ajasdf)
cast float to int, python just removes everythign after decimal value.


|     |
|     |
| rhs |
| lhs |
-------


'''


from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        operations = ["+", "-", "*", "/"]
        def operation(a: int, b: int, operator: str) -> int:
            if operator == "+":
                result = a + b
            if operator == "-":
                result = a - b
            if operator == "*":
                result = a * b
            if operator == "/":
                # a // b would give wrong answer for -6/132
                # -6//132 = -1,   int(-6/132) = 0
                result = int(a / b)
            return result


        for token in tokens:
            # perform opearation if we find an opeartor
            if token in operations:
                rhs = stack.pop()
                lhs = stack.pop()
                result = operation(lhs, rhs, token)
                stack.append(result)
            # add number to stack
            else:
                stack.append(int(token))


        return stack.pop()


