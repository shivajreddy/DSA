class Solution:
    def isValid(self, s: str) -> bool:

        hm = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        stack = []

        for char in s:
            if char in hm:
                stack.append(char)
            else:
                if len(stack) == 0 or char != hm[stack.pop()]:
                    return False

        if len(stack) > 0:
            return False
        return True

""" Notes:

1.stack is like a mug/testtube.
2. Fill the stack with open brackets, 
3. every time you enocuter a closing bracket, it should be equal to the top the stack i.e.,
    most recent bracket that went into the stack
4. EDGE CASES: when popping the stack, what if there is no items to pop i.e., extra closing bracket
    What if there are items in the stack after iterating over every bracket i.e., extra open bracket
"""