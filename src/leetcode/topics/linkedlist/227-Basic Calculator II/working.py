'''
Division: truncate to 0
There could be spaces (ignore them)
Get the full number with multiple digits

Multiplication, Division take precendence over addition and subtraction
Miltiplication & Division have same precendence


s = "3+2*2"
o = 7

s = " 3/2 "
o = 1

s = "2-3/2"
o =  1

s = "2-3*2"
o = -4

s = "1-2*3"
o = -5

s = "1*2/3"
o = 0

s = "1/2*3"
o = 0


s = " 1222 * 3"

if doing subtraction, we can perform addition with -ve value
a - b = a + (-b)


operation:
lhs (operator) rhs

- after traversing through the number perform current operation
    - but if the current operation is '*' or '/' then undo previous operation
    - prefrom current operation, and redo previous operation
    - update the prev_opeartor, prev_number,
        and the curr_operator to the opeartor that is after the end of number

when you finish traversing a number perform the prev_operation on that number.
result = 0
prev_number = None
prev_operator = None
curr_opeartor = "+"
curr_number = 3

reuslt = 3
prev_number = 3
prev_operator = "+"
curr_opeartor = "+"
curr_number = None

reuslt = 3
prev_number = 3
prev_operator = "+"
curr_opeartor = "+"
curr_number = 2

reuslt = 5
prev_number = 2
prev_operator = "+"
curr_opeartor = "*"
curr_number = 0

reuslt = 5
prev_number = 2
prev_operator = "+"
curr_opeartor = "*"
curr_number = 2

undo the previous operation
result = 5 (opposite of prev_operation) prev_number
result = 5 (-) 2
prev_result = 3
current_opeartion_result = curr_number * prev_number = 2 * 2 = 4
redo previous operation:
result = prev_result (prev_operation) current_operation_result
       = 3  + 4
       = 7

      c
s = "3+2*2"
o = 7


'''



class Solution:
    def calculate(self, s: str) -> int:

        curr = 0

        while curr < len(s) - 1:

            curr_char = s[curr]

            # ignore space
            if curr_char == ' ':
                continue
            
            if curr_char.isdigit():

                while curr < len(s)-1 and s[curr].isdigit():
                    curr += 1









































        
