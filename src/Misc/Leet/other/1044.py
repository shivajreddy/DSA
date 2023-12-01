
#! 1044. Longest Duplicate Substring

"""
Given a string s, consider all duplicated substrings: (contiguous) substrings of s that occur 2 or more times. The occurrences may overlap.

Return any duplicated substring that has the longest possible length. If s does not have a duplicated substring, the answer is "".
"""


h1 = {'a':2, 'b':3}

count = h1['a']

if count % 2 == 0:
  print(int(count/2))
else:
  print(int(count/2)+1)



