"""
### We'll take an approach that balances scalability and optimization, suitable 
for handling large inputs and ensuring performance similar to what is expected 
in a high-performance production system at a company like Amazon.

### Problem Overview:
- Given a 2D board of characters and a list of words, find all words from the 
  list that exist in the board. Each word must be constructed from letters of 
  sequentially adjacent cells, where "adjacent" cells are those horizontally or 
  vertically neighboring. The same letter cell may not be used more than once 
  in a word.

### Key Insights:

#### Backtracking:
- We can use backtracking to explore each cell on the board as a potential 
  starting point for each word. However, directly backtracking for each word 
  individually would be inefficient.

#### Trie Data Structure:
- A **Trie** (prefix tree) is ideal for storing the list of words because it 
  allows efficient prefix-based searching. With the Trie, we can:
  1. **Build the Trie** from the word list.
  2. Use the Trie to guide our backtracking process, pruning unnecessary paths 
     early when a word prefix doesn't match.

### Optimization:
- Instead of searching for each word individually (which would result in 
  redundant searches), we traverse the board once and look for all words 
  concurrently using the Trie.
- **Early stopping** is enabled by the Trie: if a prefix doesn't match any 
  word, we stop searching in that direction.

### Time Complexity:
- **Building the Trie**: `O(L)`, where `L` is the total number of characters in 
  all words.
- **Search**: In the worst case, each cell in the board is visited up to 4 
  directions, leading to a complexity of `O(M * N * 4^W)`, where `M` is the 
  number of rows, `N` is the number of columns, and `W` is the average length 
  of the words. However, the Trie optimizes and prunes unnecessary paths, 
  making this much faster in practice.

### Plan:
1. **Build the Trie**: Insert all the words into a Trie.
2. **Backtrack through the board**: For each cell, initiate a DFS-like 
   traversal, guided by the Trie. If we find a word, add it to the result.
3. **Mark visited cells**: Ensure that each cell is used only once per word by 
   marking cells as visited during the backtracking.
4. **Pruning**: Use the Trie to prune the search when a prefix is not found in 
   any of the words.


### Explanation:

#### TrieNode Class:
- This class defines each node in the Trie. Each node has a `children` 
  dictionary that stores child nodes corresponding to each character, and a 
  `word` attribute to mark the end of a word.

#### build_trie Function:
- We build the Trie by iterating over each word and inserting it into the Trie 
  character by character. The `word` attribute is set at the last character of 
  each word to indicate a complete word.

#### backtrack Function:
- For each cell, we perform a DFS-like search. If the current cell's character 
  matches the Trie, we move forward. If we find a complete word 
  (`curr_node.word`), we add it to `found_words`.
- During the search, we mark cells as visited by changing their value 
  temporarily to `'#'` to prevent revisiting.
- The search continues in all four possible directions: up, down, left, and 
  right.
- After the search completes for a path, we restore the cell's value and prune 
  the Trie by removing nodes that are no longer needed.

#### Main Search:
- We iterate over every cell in the board and, for each cell, start a 
  backtracking search if the cell’s character exists in the root of the Trie.


Example Walkthrough:
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath", "pea", "eat", "rain"]
Output: ["oath", "eat"]

- **Trie Construction**: Insert the words `["oath", "pea", "eat", "rain"]` into 
  the Trie.
  
- **Search Process**:
  - Start from each cell and try to form words using backtracking and the Trie.
  - Words `"oath"` and `"eat"` are found and added to the result set.
  - The search skips unnecessary paths quickly due to the Trie.

### Optimization:

- **Trie Pruning**: We prune the Trie by removing leaves that no longer lead to 
  valid words after each search, reducing memory usage and unnecessary checks 
  in subsequent searches.
  
- **Early Termination**: If a character doesn't exist in the Trie at any step, 
  we terminate the search in that direction early, avoiding wasteful recursion.

### Edge Cases:
- **Empty Board or Words List**: Return an empty list if the board or the words 
  list is empty.
- **Words Longer Than Board**: Words longer than the largest dimension of the 
  board will never be found and are handled naturally by the Trie.
- **No Valid Words**: If no words are found, return an empty list.

### Time and Space Complexity:

#### Time Complexity:
- **Building the Trie**: `O(L)`, where `L` is the total length of all words.
- **Backtracking Search**: In the worst case, each cell can initiate a DFS that 
  explores 4 directions for up to the length of the longest word `W`, leading 
  to a complexity of `O(M * N * 4^W)` for `M` rows, `N` columns, and word 
  length `W`. However, Trie pruning significantly reduces redundant 
  explorations.

#### Space Complexity:
- **Trie Space**: `O(L)` for storing all words.
- **Recursion Stack**: At most `O(W)` recursion depth for the backtracking 
  search, where `W` is the length of the longest word.


"""

from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Trie node definition
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.word = None

        # Build the Trie
        def build_trie(words):
            root = TrieNode()
            for word in words:
                node = root
                for char in word:
                    if char not in node.children:
                        node.children[char] = TrieNode()
                    node = node.children[char]
                node.word = word  # Mark the end of a word
            return root

        # Backtracking search
        def backtrack(r, c, parent):
            letter = board[r][c]
            curr_node = parent.children.get(letter)

            if not curr_node:
                return

            # Found a word in the trie
            if curr_node.word:
                found_words.add(curr_node.word)
                curr_node.word = None  # Avoid duplicate word findings

            # Mark the current cell as visited
            board[r][c] = '#'

            # Explore neighbors (up, down, left, right)
            for (row_offset, col_offset) in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_row, new_col = r + row_offset, c + col_offset
                if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]):
                    if board[new_row][new_col] in curr_node.children:
                        backtrack(new_row, new_col, curr_node)

            # Restore the current cell
            board[r][c] = letter

            # Prune the Trie by removing the leaf nodes that are no longer necessary
            if not curr_node.children:
                parent.children.pop(letter)

        # Step 1: Build the Trie from the word list
        trie_root = build_trie(words)

        # Step 2: Prepare for backtracking
        found_words = set()  # Set to avoid duplicates
        rows, cols = len(board), len(board[0])

        # Step 3: Backtrack for each cell in the board
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in trie_root.children:
                    backtrack(r, c, trie_root)

        return list(found_words)


