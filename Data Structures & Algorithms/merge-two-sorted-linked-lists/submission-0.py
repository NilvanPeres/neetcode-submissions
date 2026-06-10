# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # Tem dois edges cases, lista vazia -> resolva com o dummy. E o da quantidade elementos das listas serem diferentes
        # aí nesse caso precisa pegar o que restou e adicionar ao final

        dummy = ListNode()
        tail = dummy

        current_list_one = list1
        current_list_two = list2


        while current_list_one and current_list_two:
            # Se a segunda lista é menor primeiro o current deve apontar para 2 e dps para a primeira e avançar
            next_value_list_one = current_list_one.next
            next_value_list_two = current_list_two.next
            if current_list_one.val > current_list_two.val:
                # tail deve apontar para elem da lista 2
                tail.next = current_list_two
                current_list_two = next_value_list_two

            else:
                # tail head deve apontar para elem da lista 1
                tail.next = current_list_one
                current_list_one = next_value_list_one

            tail = tail.next # move o tail para o proximo elemento
        
        # Se uma ponteiro chegou ao final de uma lista mas não ao final de outra, add o restante
        if current_list_one:
            tail.next = current_list_one
        elif current_list_two:
            tail.next = current_list_two
            

        return dummy.next






        