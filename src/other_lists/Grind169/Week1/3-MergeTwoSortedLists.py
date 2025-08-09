# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # First create a temporary node.
        # Start with curr node as temporary node
        # Keep linking the proper nodes to this temporary node
        # update the curr node to curr.next, since a new node was added to the curr node
        # return the temporary node's next node

        temp_node = ListNode()
        curr = temp_node        # since it's an object

        while list1 and list2:
            # Attach the smallest node to curr
            if list1.val < list2.val:       # Attach the list1 node
                curr.next = list1
                list1 = list1.next
            else:                           # Attach the list2 node
                curr.next = list2
                list2 = list2.next
            curr = curr.next        # now the curr will be newly added node

        if list1:                       # list1 node exists, so attach it to curr
            curr.next = list1
        elif list2:                     # else, attach list2 to curr
            curr.next = list2

        return temp_node.next
