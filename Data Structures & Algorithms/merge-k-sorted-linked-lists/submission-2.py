# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        # Continua agrupando em pares até sobrar apenas 1 lista combinada
        while len(lists) > 1:
            merged_lists = []
            
            # Pula de 2 em 2 para pegar os pares
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                # Verifica se existe um par para a lista atual, senão passa None
                list2 = lists[i+1] if (i + 1) < len(lists) else None
                
                merged_lists.append(self.mergeTwoLists(list1, list2))
            
            # Atualiza a lista original com os resultados dos merges desta iteração
            lists = merged_lists

        return lists[0]

    def mergeTwoLists(self, list1, list2) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next 

        if list1:
            tail.next = list1
        if list2:
            tail.next = list2

        return dummy.next