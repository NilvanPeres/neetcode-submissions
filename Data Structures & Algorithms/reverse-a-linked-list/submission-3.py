# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Iterative two pointers

        # Time complexity O(N) and space complexity O(1)
        current = head
        previous = None

        while current:

            next_node = current.next #Guardar o próximo nó (pois vai ser quebrado a lista para reordenar os ponteiros)

            current.next = previous #O cur.next -> aponta para o previous
            previous = current # Agora o previous vai ser o nó current 

            current = next_node #Atualiza current para andar na lista

        return previous


        