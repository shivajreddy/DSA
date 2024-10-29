"""
### Data Structures:
- **Hashmap (hm)**: Stores key-node pairs for `O(1)` access to any node.
- **Doubly Linked List (DLL)**: Maintains the order of the elements with the 
  most recently accessed nodes at the front.
  - The **head** is a placeholder before the most recently accessed node.
  - The **tail** is a placeholder after the least recently accessed node.

### Core Operations:
- **Get operation (`get()`)**: 
  - If the key exists, move the node to the front (most recently accessed 
    position) and return the value.
  - If the key doesn't exist, return `-1`.
- **Put operation (`put()`)**: 
  - If the cache is full and a new item is added, the least recently used item 
    (the node before the tail) is removed.
  - The new node is then added to the front.

### Auxiliary Methods:
- **`push()`**: Adds a node right after the head to signify that it's the most 
  recently used.
- **`pop()`**: Removes the node just before the tail, which is the least 
  recently used.

### Time Complexity:
- **`get()`**: `O(1)` for accessing the hashmap and rearranging nodes in the 
  doubly linked list.
- **`put()`**: `O(1)` for updating or adding a new node, evicting if necessary.

### Space Complexity:
- `O(n)`, where `n` is the capacity of the cache. We store up to `n` nodes in 
  both the hashmap and the doubly linked list.

### Improvements for Production:
- **Error Handling**: Add safeguards for incorrect inputs, e.g., invalid key 
  types.
- **Concurrency**: Ensure thread safety if used in a multi-threaded environment.
- **Unit Testing**: Implement test cases for edge cases (e.g., `put()` and 
  `get()` operations when the cache is full).
- **Enhance Efficiency**: The current implementation is efficient, but for very 
  large capacity sizes, we could explore more cache-friendly data structures.

"""



class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class DLL:
    def __init__(self):
        self.size = 0
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        """
        Remove a node from its current position in the doubly linked list.
        """
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        self.size -= 1

    def push(self, node):
        """
        Insert a node at the front (right after the head).
        """
        head, nxt = self.head, self.head.next
        head.next = node
        node.prev = head
        node.next = nxt
        nxt.prev = node
        self.size += 1

    def pop(self):
        """
        Remove the least recently used element (the node before the tail).
        """
        target = self.tail.prev
        if target != self.head:  # Ensure we're not removing the head
            self.remove(target)
            return target
        return None




class LRUCache:


    def __init__(self, capacity: int):
        """
        Initialize the LRUCache with a given capacity.
        """
        self.capacity = capacity
        self.cache = DLL()  # Doubly linked list to track usage
        self.hm = {}        # Hashmap to map keys to nodes

    def get(self, key: int) -> int:
        """
        Get the value of the key if the key exists in the cache, otherwise return -1.
        """
        if key not in self.hm:
            return -1

        node = self.hm[key]
        self.cache.remove(node)  # Remove the node from its current position
        self.cache.push(node)    # Move it to the front (mark as recently used)
        return node.val


    def put(self, key: int, value: int) -> None:
        """
        Add or update the value of the key. If the number of keys exceeds the capacity,
        evict the least recently used key.
        """
        if key in self.hm:
            # Remove the existing node (because we're updating the value)
            node = self.hm[key]
            self.cache.remove(node)

        # If the cache is full, evict the least recently used (LRU) node
        if self.cache.size == self.capacity:
            lru_node = self.cache.pop()
            if lru_node:
                del self.hm[lru_node.key]

        # Insert the new node or update the existing node's value
        new_node = Node(key, value)
        self.cache.push(new_node)
        self.hm[key] = new_node




