class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        hm = {
            "(": ")",
            "[": "]",
            "{": "}",
        }

        for char in s:
            if char in hm:
                stack.append(char)
            else:
                if not stack or hm[stack.pop()] != char:
                    return False

        if stack:
            print("here")
            return False

        return True
