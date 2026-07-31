class ListNode:
    def __init__(self, val: str):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = ListNode("0")
        self.tail = ListNode("0")
        self.homepage = ListNode(homepage)

        self.head.next = self.homepage
        self.tail.prev = self.homepage

        self.homepage.next = self.tail
        self.homepage.prev = self.head

        self.index = 0 # Mantem o index

        self.current = self.homepage # ponteiro para nó atual
        
    def visit(self, url: str) -> None:
        # Visit perde td para frente
        
        new_node, next, previous = ListNode(url), self.tail, self.current # Lembrando que 'next' e 'previous' serão os nós em relação a nova estrutura a ser adicionada

        previous.next = new_node # meu current tem q apontar para o novo nó
        next.prev = new_node # o tail precisa apontar para o novo nó. Aqui acontece onde o "reset"

        new_node.next = next
        new_node.prev = previous

        # Atualiza current para o novo nó
        self.current = new_node
        

    def back(self, steps: int) -> str:
        
        while (steps > 0 and self.current.prev != self.head):
            steps -= 1
            self.current = self.current.prev

        return self.current.val

    def forward(self, steps: int) -> str:
        while (steps > 0 and self.current.next != self.tail):
            steps -= 1
            self.current = self.current.next

        return self.current.val


        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)