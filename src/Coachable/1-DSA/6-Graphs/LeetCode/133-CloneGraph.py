import collections


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        if not node: return node

        # using BFS
        q = collections.deque([node])  # deque to store all the nodes we encounter

        '''
        {
            <original_node_1> : <copy_node_1>,
            <original_node_2> : <copy_node_2>
        }
        '''
        visited = {}
        visited[node] = Node(node.val)  # duplicate the given node
        while q:
            curr = q.popleft()

            for child in curr.neighbors:
                new_child_node = Node(child.val)  # duplicate each child node
                if child not in visited:
                    q.append(child)  # add to the queue
                    visited[child] = new_child_node  # add child to visited
                visited[curr].neighbors.append(visited[child])  # add child_copy as neigh.
        return visited[node]
