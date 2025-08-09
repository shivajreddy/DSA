def non_repeat_substring(str):

  # TODO: Write your code here
    arr = [*str]
    start = 0
    hashmap = {}
    result = 0

    for end in range(len(arr)):
        item = arr[end]
        if item not in hashmap.keys():
            hashmap[item] = 1
        else:
            hashmap[item] += 1

        while 2 in list(hashmap.values()):
            # print(start,end,hashmap)
            first = arr[start]
            hashmap[first] -= 1
            if hashmap[first] == 0:
                del hashmap[first]
            start += 1

        result = max(result, end-start+1)

    return result

s = "aabccbb"
s = "abbbb"
s = "abccde"
print(non_repeat_substring(s))