"""
### Explanation:

#### Directions:
- We define the four possible directions: Up, Down, Left, and Right, as tuples 
  that are used for navigation in the grid.

#### DFS (Depth-First Search):
- A helper function `dfs` is used to recursively explore the board.
- The function searches for the word by matching one character at a time and 
  exploring adjacent cells.
- If the current character doesn't match or we go out of bounds, the search for 
  that path stops.
- The function backtracks by removing cells from the visited set when a path is 
  no longer valid.

#### Word Search:
- We iterate over each word in the input list `words`.
- For each word, the search starts at each cell in the board, checking if the 
  word can be formed starting from that cell.
- If a word is found, it is added to the result list and the search for that 
  word ends.

#### Optimization:
- If a word is found, further searching for that word is stopped to avoid 
  unnecessary computation.

### Time and Space Complexity:

#### Time Complexity: `O(N * M * 4^L)`, where:
- `N` and `M` are the dimensions of the board (rows and columns).
- `L` is the length of the longest word. For each starting position in the 
  board, we explore 4 directions for up to `L` recursive steps.

#### Space Complexity: `O(L)`, where `L` is the length of the longest word.
- This accounts for the recursive call stack and the visited set.

"""


from typing import List, Set, Tuple

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Define the four possible movement directions: Up, Down, Left, Right
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def dfs(r: int, c: int, idx: int, word: str, visited: Set[Tuple[int, int]]) -> bool:
            """
            Perform a depth-first search to find the word in the board.

            Args:
            r (int): Row index
            c (int): Column index
            idx (int): Index of the current character in the word
            word (str): The word to search for
            visited (Set[Tuple[int, int]]): Set of visited coordinates to avoid revisits

            Returns:
            bool: True if the word is found starting from (r, c), else False
            """
            # Base case: All characters matched, word is found
            if idx == len(word):
                return True

            # Check if the current position is within bounds and matches the word's character
            if not (0 <= r < R and 0 <= c < C) or board[r][c] != word[idx] or (r, c) in visited:
                return False

            # Mark the current cell as visited
            visited.add((r, c))

            # Explore all 4 possible directions
            for dr, dc in directions:
                if dfs(r + dr, c + dc, idx + 1, word, visited):
                    return True

            # Backtrack by unmarking the visited cell
            visited.remove((r, c))

            return False

        R = len(board)
        C = len(board[0])

        # Result list to store found words
        result = []

        # Iterate through each word and search it on the board
        for word in words:
            found = False
            for r in range(R):
                for c in range(C):
                    if dfs(r, c, 0, word, set()):
                        result.append(word)
                        found = True
                        break
                if found:
                    break

        return result

