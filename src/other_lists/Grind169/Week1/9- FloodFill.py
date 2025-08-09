# https://leetcode.com/problems/flood-fill/
from collections import deque


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        rows = len(image)
        cols = len(image[0])

        target = image[sr][sc]

        if target == color:
            return image

        start = (sr, sc)

        q = deque()
        q.append(start)

        while q:

            curr = q.popleft()

            x = curr[0]
            y = curr[1]

            if image[x][y] == target:
                image[x][y] = color

            # for every item in deque, if it has 4-items, add to deque

            if x-1 >= 0 and image[x-1][y] == target:
                q.append((x-1, y))
            if x+1 <= rows-1 and image[x+1][y] == target:
                q.append((x+1, y))
            if y-1 >= 0 and image[x][y-1] == target:
                q.append((x, y-1))
            if y+1 <= cols-1 and image[x][y+1] == target:
                q.append((x, y+1))

        return image
