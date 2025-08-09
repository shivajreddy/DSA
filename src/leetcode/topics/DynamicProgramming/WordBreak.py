from collections import defaultdict

s = "leetleetcode"
word = "leet"


def find_positions(word):
    start, end = 0, len(word) - 1
    result = []
    while start < len(s) and end < len(s):
        if s[start] == word[0] and s[end] == word[-1]:
            if s[start:end + 1] == word:
                result.append((start, end))
        start += 1
        end += 1
    return result


# print(find_positions("leet"))
# print(find_positions("etc"))

hm = defaultdict(list)
# hm = {}
wordDict = ["leet", "code"]
# wordDict = ["leet", "code", "shiva"]
for word in wordDict:
    results = find_positions(word)
    hm[word] = hm[word] + results

for v in hm.values():
    if not v:
        print("False")

print(hm)
