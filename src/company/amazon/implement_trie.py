'''
Assumptions:
    - `startsWith` fn finds a prefix that is a complete word, return True

### Key Concepts:

#### Trie Structure:
- A Trie is a tree-like data structure that stores words in a way that allows
  efficient retrieval of words based on their prefixes.

#### Nodes:
- Each node represents a character and has a collection of child nodes
  representing possible subsequent characters.

#### Leaf Nodes:
- Nodes that mark the end of a word.

### Plan:

#### Node Definition:
- Create a `TrieNode` class with:
  - A fixed-size array or a hashmap to store references to child nodes.
  - A boolean flag to indicate if the node represents the end of a word.

#### Trie Class Implementation:
- **Insert Method**: Traverse the Trie, creating new nodes as needed.
- **Search Method**: Traverse the Trie to check if a word exists.
- **StartsWith Method**: Traverse the Trie to check if a prefix exists.

### Performance Considerations:

- **Space Efficiency**: Use a hashmap for child nodes to handle any character set
  efficiently.
- **Time Efficiency**: Each operation should have a time complexity proportional
  to the length of the input word or prefix.

### Time and Space Complexity:

#### Insert:
- **Time Complexity**: `O(N)`, where `N` is the length of the word.
- **Space Complexity**: `O(N)`, for the new nodes created.

#### Search and StartsWith:
- **Time Complexity**: `O(N)`, where `N` is the length of the word or prefix.
- **Space Complexity**: `O(1)`, as we are not allocating additional space
  proportional to the input size.

'''
class TrieNode:
    def __init__(self):
        self.children = {}  # Mapping from character to TrieNode
        self.is_end_of_word = False  # True if the node represents the end of a word

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Inserts a word into the trie."""
        node = self.root
        for char in word:
            # If the character is not already a child, add a new TrieNode
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]  # Move to the child node
        node.is_end_of_word = True  # Mark the end of a word

    def search(self, word: str) -> bool:
        """Returns True if the word is in the trie."""
        node = self._search_prefix(word)
        return node is not None and node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        """Returns True if there is any word in the trie that starts with the given prefix."""
        return self._search_prefix(prefix) is not None

    def _search_prefix(self, prefix: str):
        """Helper function to traverse the trie up to the end of the given prefix."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None  # Prefix not found
            node = node.children[char]
        return node


'''
### Explanation:

#### TrieNode Class:
- `children`: A dictionary mapping characters to their corresponding child
  `TrieNode`. Using a dictionary allows for efficient insertion and search
  without wasting space on unused characters.
- `is_end_of_word`: A boolean flag to indicate whether a node marks the end of
  a word.

#### Trie Class:

- **insert(word)**:
  - Start from the root node.
  - For each character in the word:
    - If the character is not present among the current node's children, create
      a new `TrieNode` and add it to the children.
    - Move to the child node corresponding to the character.
  - After inserting all characters, mark the last node as `is_end_of_word = True`.

- **search(word)**:
  - Use the helper method `_search_prefix` to traverse the trie up to the end
    of the word.
  - If the traversal returns a node and `is_end_of_word` is `True`, the word
    exists in the trie.

- **startsWith(prefix)**:
  - Use the helper method `_search_prefix` to traverse the trie up to the end
    of the prefix.
  - If the traversal returns a node, the prefix exists in the trie.

- **_search_prefix(prefix)**:
  - Start from the root node.
  - For each character in the prefix:
    - If the character is not among the current node's children, return `None`.
    - Move to the child node corresponding to the character.
  - Return the node reached after traversing the prefix.
'''


# TESTS
# Example usage:
trie = Trie()

# Insert words
trie.insert("apple")
trie.insert("app")
trie.insert("application")

# Search for words
print(trie.search("app"))         # True
print(trie.search("apple"))       # True
print(trie.search("apples"))      # False
print(trie.search("application")) # True

# Check prefixes
print(trie.startsWith("app"))     # True
print(trie.startsWith("appl"))    # True
print(trie.startsWith("banana"))  # False


'''
### Edge Cases and Considerations:

- **Empty String**:
  - The implementation can handle empty strings. Inserting an empty string will
    set `is_end_of_word` at the root node.

- **Case Sensitivity**:
  - The trie is case-sensitive. If case-insensitive behavior is desired, convert
    the input strings to lower or upper case during insertion and search.

- **Non-alphabetic Characters**:
  - The trie supports any character as keys in the `children` dictionary,
    including numbers and symbols.

- **Memory Usage**:
  - Using a dictionary for `children` optimizes memory usage by only storing
    necessary child nodes.

### Optimization Notes:

#### Use of Dictionaries vs Fixed Arrays:
- While a fixed-size array (e.g., of size 26 for lowercase English letters) can
  be faster due to direct indexing, it can waste space when the character set is
  large or sparse.
- Using dictionaries allows us to handle any character set efficiently, which is
  important for scalability in real-world applications where inputs may include
  Unicode characters or a large set of symbols.

#### Lazy Deletion:
- In a full implementation, we might want to support deletion of words. This can
  be added with careful handling to remove nodes that are no longer needed.
'''

