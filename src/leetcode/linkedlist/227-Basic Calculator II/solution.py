"""
# 227 - Basic Calculator II
[LeetCode](https://leetcode.com/problems/basic-calculator-ii/description/)


TimeStamps:
1. Understand the Problem: 00:00 - 00:00 (00 MIN)
2. Design&Verify Solution: 00:00 - 00:00 (00 MIN)
3. Code & Pass Test Cases: 00:00 - 00:00 (00 MIN)
"""

'''
Problem:
    - Can't use eval() inbuilt methods
    - given operations ('+', '-', '*', '/')
    - input length is >= 1
    - All intermediate results will be in the range of [-231, 231 - 1]

Assumptions:
 - given expression is always valid
 - no space in b/w multi-digit number
 - input neither starts with operator, nor ends with operator
 - there won't be division by 0

Observations:
    - double digit numbers
    - there could be empty white spice before/after the operator
    - even though we are only given +ve integers, intermediate results could be -ve,  
        so we can't use floor division when there is a -ve numerator.
        Instead use  int(numerator/denominator)
    - lhs, rhs  position matters (especially for subraction and division)

    - not entirely BODMAS (Division, Multiplication, Addition, Subtraction)
        input = "3 * 3 / 2"   output = 4
        input = "3 / 2 * 4"   output = 2
        so, multiplication or division have equal weightage, and they preceed +,-


Test Case:

prev -> track the previously encountered number
prev_operation -> track the previously done operation

treat '-' as also addition, i.e., a - b => a + (-b)


p  = None
po = None
      c
IN : "3+2 *2"
OUT: 7

IN : "3/2*2+2*3"
OUT: 7


IN : "1"
OUT: 1

IN : "1/2"
OUT: 0

IN : "1 / 2"
OUT: 0

IN :"1 - 2"
OUT: 3

'''

class Solution:

    def perform_operation(self, lhs: int, rhs: int, operator: str) -> int:
        if operator == "+":
            return lhs + rhs
        if operator == "-":
            return  lhs - rhs
        if operator == "*":
            return lhs * rhs
        if operator == "/":
            return int(lhs / rhs)
        return -1


    def calculate(self, s: str) -> int:

        lhs = None
        rhs = None
        prev_operation = None

        curr_num_str = ""

        for curr_char in s:
            # ignore empty space
            if curr_char == " ":
                continue
            
            if curr_char.isnumeric():
                curr_num_str += curr_char
            else:
                # create lhs if not already created
                if lhs is None:
                    lhs = int(curr_num_str)
                    curr_num_str = ""
                    prev_operation = curr_char
                # lhs was already created, so number is rhs
                else:
                    rhs = int(curr_num_str)
                    curr_num_str = ""

                    result = self.perform_operation(lhs, rhs, prev_operation)

                    lhs = result
                    rhs = None
                    prev_operation = curr_char
        
        if prev_operation is None:
            return lhs
        
        rhs = int(curr_num_str)
        result = self.perform_operation(lhs, rhs, prev_operation)

        return result
            


class Solution:

    def calculate(self, s: str) -> int:

        i = 0

        # curr, prev, res = 0, 0, 0
        curr = prev = res = 0
    
        curr_operation = "+"
    
        while i < len(s):
    
            curr_char = s[i]
    
            # found a space
            # if curr_char == ' ':
            #     i += 1
            #     continue
    
            # found a digit
            if curr_char.isdigit():
    
                while i < len(s) and s[i].isdigit():
                    curr = curr * 10 + int(s[i])
                    i += 1
    
                i -= 1
    
                if curr_operation == "+":
                    res += curr
                    prev = curr
                elif curr_operation == "-":
                    res -= curr
                    prev = -curr
                elif curr_operation == "*":
                    res -= prev
                    res += prev * curr
                    prev = prev * curr
                else:
                    res -= prev
                    res += int(prev / curr)
                    prev = int(prev / curr)
    
                curr = 0
    
            elif curr_char != " ":
                curr_operation = curr_char
    
            i += 1
    
        return res
