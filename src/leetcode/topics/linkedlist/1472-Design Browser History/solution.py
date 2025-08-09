class Node:
    def __init__(self, val: str, prev: 'Node | None' = None, next: 'Node | None' = None, ) -> None:
        self.val = val
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = Node("")
        self.tail = Node("")
        self.head.next, self.tail.prev = self.tail, self.head   # head <-> tail

    def add(self, curr_node: Node | None, new_node: Node) -> None:
        if curr_node is None:
            curr_node = self.head
        # head <-> ... curr <-> nxt ... <-> tail
        nxt = curr_node.next
        curr_node.next, nxt.prev = None, None                   # curr |  nxt ... <-> tail  #type: ignore
        curr_node.next, new_node.prev = new_node, curr_node     # curr <-> new_node
        self.tail = None                                        # nxt ... None
        self.tail = Node(-1, -1)                                # curr <-> new_node    |  tail  #type: ignore
        new_node.next, self.tail.prev = self.tail, new_node     # curr <-> new_node <-> tail


class BrowserHistory:

    def __init__(self, homepage: str):
        home_node = Node(homepage)
        self.urls = [home_node]
        self.history = DoublyLinkedList()
        self.history.add(None, home_node)
        self.curr = 0   # tracks the current position(idx) on the urls

    def visit(self, url: str) -> None:
        del self.urls[self.curr + 1:]    # remove everything after the curr position
        curr_node = self.urls[self.curr]
        new_node = Node(url)
        self.history.add(curr_node, new_node)   # add new-url-node to history, after curr-node
        self.urls.append(new_node)              # add to list of urls
        self.curr += 1                          # move curr position to the newly visited url
        self.curr = len(self.urls) - 1 # or point to the last url bcs

    def back(self, steps: int) -> str:
        if steps >= self.curr:
            self.curr = 0
        else:
            self.curr -= steps
        node = self.urls[self.curr]
        return node.val

    def forward(self, steps: int) -> str:
        N = len(self.urls)
        if steps + self.curr >= N - 1:
            self.curr = N - 1
        else:
            self.curr += steps
        node = self.urls[self.curr]
        return node.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
