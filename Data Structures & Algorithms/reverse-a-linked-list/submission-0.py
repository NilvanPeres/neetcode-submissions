# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Iterar sobre a lista encadeada (Solução vai ser O(N) no melhor cenário)
        # 2. Precisa retornar a lista em modo reverso:
            # Ex:
            # input: head -> 0 -> 1 -> 2 -> 3 -> tail
            # output: head -> 3 -> 2 -> 1 -> 0 -> tail
        # 3. Posso usar pilha para armazenar a nova ordem para a forma reversed

        stack = []
        current = head
        while current:
            stack.append(current.val)
            current = current.next

        tamanho_pilha = len(stack)

        if stack: 
            new_value = stack.pop()
            new_head = ListNode(new_value)
            current = new_head

            while stack:
                current.next = ListNode(stack.pop())
                current = current.next

            return new_head
      
            

            
        