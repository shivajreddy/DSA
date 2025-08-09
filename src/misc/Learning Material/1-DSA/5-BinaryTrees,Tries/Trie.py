# Tries

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class Trie:

    def __init__(self):
        self.root = TrieNode()  # the root of Trie is a dummy root node

    def insert(self, word: str) -> None:
        curr_node = self.root

        for char in word:
            if char not in curr_node.children:
                curr_node.children[char] = TrieNode()
            curr_node = curr_node.children[char]

        curr_node.end_of_word = True  # mark the last node as "end_of_word"

    def search(self, word: str) -> bool:
        curr_node = self.root

        for char in word:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]
        return curr_node.end_of_word  # return True only if this char is end_of_word

    def starts_with(self, prefix: str) -> bool:
        curr_node = self.root

        for char in prefix:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]
        return True
