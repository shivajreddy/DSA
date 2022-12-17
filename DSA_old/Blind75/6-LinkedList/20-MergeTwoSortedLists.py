# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()

        curr = dummy

        while l1 and l2:

            # 1. check for smalled node
            # 2. add that smallest to curr's next
            # 3. move that smallest node to it's next

            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next

            # no matter which node's list we added to curr
            # move the curr pointer to its next
            curr = curr.next

            # check if any of the lists still have nodes
            # if so, add those to the curr's next
            if l1:
                curr.next = l1
            elif l2:
                curr.next = l2

        # now the curr is pointing the very last or some where in middle,
        # cuz we just added all remaining ndoes. but the dummy pointer still holds a
        # ref to the empty node we initialized, and we can simply return the next of it
        return dummy.next


    """Notes:
    
    1. concept of creating a dummy node
    2. start a curr pointer, starting with referring to the dummy node
    3. curr's next should be the smallest of the two list's nodes
    4. no matter which list was smaller, since it was added as next, now move the curr pointer to the last added node
    5. if any of the lists have no more nodes remaining, other list might have some remaining, so check which has then link that start to curr's next
    6. now return the first created dummy node's next, because we just added all remaining ndoes. but the dummy pointer still holds a
        ref to the empty node we initialized, and we can simply return the next of it
        
    """