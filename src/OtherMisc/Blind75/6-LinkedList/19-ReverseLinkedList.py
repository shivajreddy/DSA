# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # you need
        p = None
        c = head

        while c:
            n = c.next
            c.next = p

            # current is None, and loop stops, last node is the p pointer node
            p = c
            c = n

        return p

        p = None
        c = head


""" Notes:
You always, ONLY need two pointers to change the connections in a linked list.

Order of this problem:
1. change the link of current. i.e., c.next = p
2. now point the 'p' pointer to current node. -> p = c
3. point the 'c' pointer to c's next. -> c = c.next -> but since c.next is already changed in 1. all we have to do before making this change
    save the c.next into a temp pointer, so your very first step is -> n = c.next
    now use use this 'n', -> c = n
4. after all nodes finishes, c will be pointing to None, p will be pointing to the last node. So return p

"""