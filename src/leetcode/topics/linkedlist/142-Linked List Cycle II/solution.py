'''
TimeStamps:
1. Understand the Problem: 00:00 - 00:00 (00 MIN)
2. Design&Verify Solution: 00:00 - 00:00 (00 MIN)
3. Code & Pass Test Cases: 00:00 - 00:00 (00 MIN)


(if cycle exists)
two pointers to find the meeting node
    (if not) return None


two pointers, starting from head and meeing-node, move by 1, until they meet
- they meet at the common 


'''

from typing import Optional

class ListNode:
    def __init__(self, val, next = None) -> None:
        self.val = val
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:


        # two pointers, whare fast moves at 2x speed
        # slow moves at 1x speed

        # dummy = ListNode(-1)
        # dummy.next = head
        # slow, fast = dummy, dummy 

        slow, fast = head, head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            # there is a cycle and slow met fast
            if slow == fast:
                break

        
        # fast reached None, meaning, there is no cycle
        if fast is None or fast.next is None:
            return None
        
        # dist. b/w head to the 1st cycle node == dist. b/w meeting-node to the 1st cycle node
        # start another slow poiner at the head of the List
        # both slow, and slow2 move by 1x speed

        slow2 = head
        while slow != slow2:

            slow = slow.next
            slow2 = slow2.next
        
        return slow
