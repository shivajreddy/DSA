# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head, nxt):

  if not head or not head.next:
    return head
  
  curr = head
  newHead = nxt
  nxt.next = curr

  return reverseList(newHead, newHead.next)

  first = head
  second = first.next

  if not second:
    return first

  third = second.next

  second.next = first

  # Leaf node -> Base condition
  if not head.next:
    return head 
  
  leaf = reverseList(head)
  return 