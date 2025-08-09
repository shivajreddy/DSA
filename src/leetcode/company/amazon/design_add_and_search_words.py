"""
Approach:
	- We use a Trie (Prefix Tree) to efficiently store and search words. Each node in the Trie represents a character,
    and paths from the root to a node represent prefixes of words. For the search operation, we handle the
    wildcard character '.' by recursively exploring all possible paths when a '.' is encountered.

Time Complexity:
	- addWord: O(n), where n is the length of the word being added.
	- search: Worst-case O(m^n), where m is the number of possible characters (26 for lowercase letters) and n is the
      length of the word, due to the wildcard character exploration. However, in practice, the search operation is efficient.

Space Complexity:
	- O(total_characters), where total_characters is the sum of all characters in the words added to the Trie.

Edge Cases:
	- Empty String: Not applicable as per constraints (word.length >= 1).
	- Wildcard Only: Searches like '....' will explore all words of length 4.

Future Improvements:
	- Optimize the search by pruning unnecessary branches.
	- Implement iterative search to avoid potential stack overflow with very deep recursion.
	- Use a more memory-efficient Trie representation.
"""

from typing import Dict

class TrieNode:
    def __init__(self):
        # Each node contains a dictionary of child nodes and a flag to indicate if it's the end of a word.
        self.children: Dict[str, TrieNode] = {}
        self.end_of_word: bool = False

class WordDictionary:
    """
    A data structure that supports adding words and searching for words with support for wildcard characters.
    """

    def __init__(self):
        """Initializes the WordDictionary object"""
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """Adds a word to the data structure"""
        current = self.root
        for char in word:
            # If the character is not already a child of the current node, add it.
            if char not in current.children:
                current.children[char] = TrieNode()
            # Move to the child node corresponding to the character.
            current = current.children[char]
        # After adding all characters, mark the current node as the end of a word.
        current.end_of_word = True

    def search(self, word: str) -> bool:
        """Searches for a word in the data structure, which may contain '.' as a wildcard character"""
        return self._search_in_node(word, self.root)

    def _search_in_node(self, word: str, node: TrieNode) -> bool:
        """Recursively searches for a word starting from a given Trie node"""
        for i, char in enumerate(word):
            if char == '.':
                # return any(self._search_in_node(word[i+1:], child) for child in node.children.values())
                # If the character is a '.', check all possible child nodes.
                for child in node.children.values():
                    if self._search_in_node(word[i + 1:], child):
                        return True
                # If no child paths lead to a match, return False.
                return False
            else:
                # If the character is not found among the children, return False.
                if char not in node.children:
                    return False
                # Move to the next node corresponding to the character.
                node = node.children[char]
        # After processing all characters, check if the current node marks the end of a word.
        return node.end_of_word

