class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        # create a hashmap
        # keys = opening brackets, values = closing brackets
        hm = {'(': ')', '[': ']', '{': '}'}

        # use stack
        stack = []

        for char in s:
            # keep adding opening brackets to stack
            if char in hm:
                stack.append(char)
            else:
                # if the last item in stack is not matching return False
                if not stack or char != hm[stack[-1]]:
                    return False
                # if it was a matching pair, pop the last item
                stack.pop()
        # If stack is empty return True, not empty return False
        return not stack
