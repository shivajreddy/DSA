# 14. Longest Common Prefix

strs = ["flower","flow","flight"]

test = strs[0]
result = ""
for i in range(len(test)):
    char = test[i]

    for j in range(200):
        word = strs[j]
        if word[i] != char:
            return result
    result += char
