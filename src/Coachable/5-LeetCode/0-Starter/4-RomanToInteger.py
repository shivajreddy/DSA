class Solution:
    def romanToInt(self, s: str) -> int:
        hm = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0
        # iterating from last
        for i in range(len(s) - 1, -1, -1):
            curr = s[i]
            # if the previous counted value is bigger than current
            # then the current value should be removed from total
            # for 'IX' if previous inserted was 'X', and now we found 'I'
            # which is smaller, so remove 1 from 10, since 'IX' is 10-1
            if i + 1 < len(s) and hm[s[i + 1]] > hm[curr]:
                total -= hm[curr]
            else:
                total += hm[curr]
        return total
