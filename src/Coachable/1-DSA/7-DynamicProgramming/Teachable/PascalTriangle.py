class Solution:
    def generate(self, numRows: int) -> list[list[int]]:

        """ Bruteforce
        ''' Explanation
        result = [[1], [1,1]]

        next step: take prev step
        prev = [1,1]
        next = prev[0] + [new_items] + prev[-1]
        new_items = (prev[0] + prev[1]), (prev[1] + prev[2]), ..., (prev[n-1] + prev[n])

        add next to result:
        result = [[1], [1,1], [1,2,1]]

        '''
        result = [[1], [1, 1]]
        if numRows <= 2:
            return result[:numRows]

        for _ in range(2, numRows):
            prev = result[-1]
            new = [prev[0]]
            for idx in range(1, len(prev)):
                new.append(prev[idx - 1] + prev[idx])
            new.append(prev[-1])
            result.append(new)

        return result
        # """

        # """ DP: top-down

        triangle = []

        for idx in range(numRows):
            row = [None] * (idx + 1)  # 0: [None], 1: [None, None], 2: [None, None, None]
            row[0], row[-1] = 1, 1  # both ends are always 1

            for col in range(1, idx):  # col should go form [1, here, ... , tohere, 1]
                row[col] = triangle[idx - 1][col - 1] + triangle[idx - 1][col]

            triangle.append(row)

        return triangle

        # """
