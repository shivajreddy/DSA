# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow, fast = head, head

        while fast and fast.next:

            # check if slow and fast meet
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False



# approach 2 -> using hashmap
class solution:
    def hascycle(self, head: optional[listnode]) -> bool:

        hm = {}

        while head:
            if head in hm:
                return True
            hm[head] = 1
        return False




# approach 3 -> just emptying the value
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        while head:

            if head.val != None:
                head.val = None
            else:
                return True
        return False


"""Notes:
Approach 1:
For cycled lists:
Time : O(n-1) -> O(n). cuz fast pointer is moving twice the fast, so even before slow pointer reaching the final node in the loop

for no-cycle lists:
Fast pointer will reach None, in n/2 itself


Approach 2:
objects are hashable in python, so you can use the object as a key
you can check if the same object is in the hm already


Apprach 3:
when emptying a value, if you just do ` if head.val:` then it would equate to False when the val is 0,
so you should check it's value None, not 0

"""