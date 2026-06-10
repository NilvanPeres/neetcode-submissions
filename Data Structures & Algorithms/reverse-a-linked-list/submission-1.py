# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Caso base ? Quando o next aponta para o null == tail. OU quando o head for null também !!
        current = head
        if current is None or current.next is None:
            return current

        # Caso recursivo
        new_head = self.reverseList(current.next)  # resolve o resto primeiro
        current.next.next = current                # daí conecta o atual
        current.next = None                        # quebra o elo original
        return new_head                            # retorna o novo head




            
        