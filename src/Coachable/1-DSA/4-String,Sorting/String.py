"""
Must know in-built methods for string's in python
"""

name = "shiva"

# to char array
name_char_array = list(name)  # ['s', 'h', 'i', 'v', 'a']

original = "shiva reddy"
copy = ""
copy2 = []

for char in original:
    copy += char
    copy2.append(char)

print(original)
print(copy)
print(copy2)
