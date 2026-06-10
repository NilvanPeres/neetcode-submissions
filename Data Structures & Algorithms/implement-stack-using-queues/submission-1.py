class Node:
    def __init__(self, val: int):
        self.val = val

        self.next = None
        self.prev = None

class MyStack:

    def __init__(self):

        ## Dummy nodes
        self.head = Node(0)
        self.tail = Node(0)

        ## Ligações
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def push(self, x: int) -> None:
        # Precisa adicionar no tail/fim
        new_node, next, previous = Node(x), self.tail, self.tail.prev

        #Atualiza ligações antigas
        next.prev = new_node
        previous.next = new_node

        # Novas ligações
        new_node.next = next
        new_node.prev = previous

        print("Novo nó: ", new_node.val)
        print("Antigo último nó: ", previous.val)

    def pop(self) -> int:
        if self.tail.prev == self.head:
            return None

        node_to_remove, previous = self.tail.prev, self.tail.prev.prev

        self.tail.prev = previous
        previous.next = self.tail

        return node_to_remove.val
        

    def top(self) -> int:
        if self.tail.prev == self.head:
            return None

        print("Cabeça: ", self.tail.val)
        return self.tail.prev.val

    def empty(self) -> bool:
        return self.head.next == self.tail


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(10)
# print(obj)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()