# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head
        # Recursivo. Qual base case ?

        # Se nó atual for nulo OU se o próximo aponta para null
        if (current == None or current.next == None):
            return current

        new_head = self.reverseList(current.next)

        # Fazer inversão pensando no último caso
        # 1 -> 2 -> 3 -> None - Nesse exemplo a pilha vai ser executado a partir do 2. Pois o 3 cai no base case
        current.next.next = current # 2.next --> 3.next . Ou seja o 3 vai apontar para o 2
        current.next = None # Quebra curr.next para apontar para 
        
        return new_head


        
        