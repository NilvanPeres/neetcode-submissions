# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head
        # Caso base
        if (current == None or current.next == None):
            return current

        new_head = self.reverseList(current.next)
        current.next.next = current
        current.next = None
        return new_head
