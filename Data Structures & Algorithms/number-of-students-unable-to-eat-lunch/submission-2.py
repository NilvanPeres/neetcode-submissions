class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None
        self.prev = None

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        if len(students) <= 0:
            return 0

        head = ListNode(students[0])
        current = head

        for i in students[1:]:
            novo_no = ListNode(i)
            current.next = novo_no
            novo_no.prev = current
            current = current.next

        current = head
        sem_match_seguidos = 0
        tamanho_fila = len(students)

        while sandwiches and sem_match_seguidos < tamanho_fila:

            if current.val == sandwiches[0]:
                sandwiches.pop(0)

                previous, nextx = current.prev, current.next

                # Desconecta current da lista, tratando as pontas
                if previous is not None:
                    previous.next = nextx
                else:
                    head = nextx  # current era o head, atualiza head

                if nextx is not None:
                    nextx.prev = previous
                # se nextx for None, current era o último nó, não tem o que atualizar

                tamanho_fila -= 1
                sem_match_seguidos = 0
                current = nextx if nextx is not None else head

            else:
                sem_match_seguidos += 1
                current = current.next if current.next is not None else head

        return len(sandwiches)