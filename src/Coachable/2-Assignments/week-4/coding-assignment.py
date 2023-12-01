"""

To find the alphabetically the smallest subsequence of length n in a string, we can use the following approach:

Initialize an empty result string.
Loop through each character in the string s.
If the result string already contains n characters or the current character is less than the last character in the result string, remove the last character from the result string until it is either empty or the last character is less than the current character.
Add the current character to the end of the result string.
If the length of the result string is greater than n, remove the first character.
Return the result string.
Here's the code implementing the above approach:
"""


def smallest_subsequence(s: str, n: int) -> str:
    result = ""
    for i in range(len(s)):
        while result and len(result) + len(s) - i > n and result[-1] > s[i]:
            result = result[:-1]
        if len(result) < n:
            result += s[i]
    return result


"""
Note that the time complexity of this approach is O(len(s) * n) because of the nested while loop.
However, for small values of n and relatively short strings, the performance should be acceptable.
"""
