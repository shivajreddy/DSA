import collections
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        '''
        # using dfs
        n = len(rooms)
        visited = [False] * n
        stack = [0]

        while stack:

            room_key = stack.pop()

            if not visited[room_key]:
                new_keys = rooms[room_key]
                visited[room_key] = True

                for key in new_keys:
                    if not visited[key]:
                        stack.append(key)

        return False if False in visited else True
        '''

        # using BFS (PREFERRED)
        n = len(rooms)
        q = collections.deque([0])  # holds all the rooms to visit
        visited = [False] * n

        while q:
            curr_key = q.popleft()
            if not visited[curr_key]:
                visited[curr_key] = True

                new_keys = rooms[curr_key]

                for key in new_keys:
                    if not visited[key]:
                        q.append(key)
        return False if False in visited else True
