class LinkedListNode:
    def __init__(self, val: str):
        self.val = val
        self.prev = None #Estrutura de nó de lista encadeada
        self.next = None #Estrutura de nó de lista encadeada

class BrowserHistory:

    def __init__(self, homepage: str):

        self.homepage = LinkedListNode(homepage)

        # Cria os dummies nodes
        self.head = LinkedListNode("0")
        self.tail = LinkedListNode("0")
        
        # Linka os dummies e homepage
        self.head.next = self.homepage
        self.tail.prev = self.homepage

        #Linka homepage para ter lista duplamente encadeada
        self.homepage.prev = self.head
        self.homepage.next = self.tail

        # Aponta em qual nó está os avanços ou para retroceder
        self.curr = self.homepage

    def visit(self, url: str) -> None:
        # O visit sempre vai adicionando após o ponteiro do current
        # Edge case: It clears up all the forward history.

        new_node, next, previous = LinkedListNode(url), self.tail, self.curr # O next = self.tail pois para frente sempre será descartado. E previous será onde estava apontando para ultimo nó vaĺido

        # Aualiza 'links/ligações' dos nós antigos para novo nó
        next.prev = new_node
        previous.next = new_node

        # Coloca ligações do novo nó
        new_node.next = next # linka para o next ser o nó dummy
        new_node.prev = previous # linka ao antigo último

        # Aponta o novo nó
        self.curr = new_node
        

    def back(self, steps: int) -> str:
        # Voltando X steps a partir do ponteiro do self.curr atual
        
        while (self.curr and self.curr.prev != self.head and steps > 0): # Precisa para antes de chegar no dummy por isso self.curr.prev difrente de head... !
            self.curr = self.curr.prev
            steps -= 1
    
        return self.curr.val
            
        

    def forward(self, steps: int) -> str:
        # avança X steps, a partir do current atual

        while (self.curr and self.curr.next != self.tail and steps > 0): # Atualiza e não cai no nó dummy
            self.curr = self.curr.next
            steps -= 1

        return self.curr.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)