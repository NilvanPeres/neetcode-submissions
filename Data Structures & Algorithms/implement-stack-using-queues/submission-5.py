class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None
        self.prev = None

class MyStack:

    def __init__(self):
        
        # Dummy nodes
        self.head = ListNode(0)
        self.tail = ListNode(0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def push(self, x: int) -> None:
        # Add to tail
        new_node, next, previous = ListNode(x), self.tail, self.tail.prev

        # Atualiza ligações antigas para apontar para o novo nó
        next.prev = new_node
        previous.next = new_node

        # Linka novo nó as estruturas pŕevias
        new_node.next = next
        new_node.prev = previous

    def pop(self) -> int:
        # Remove ult elemento
        node_to_remove, next, prev = self.tail.prev, self.tail, self.tail.prev.prev

        # Remove referência do antigo último elemento
        next.prev = prev
        prev.next = next

        return node_to_remove.val

    def top(self) -> int:
        return self.tail.prev.val

    def empty(self) -> bool:
        print("o next do head: ", self.head.next.val)
        if (self.head.next != self.tail):
            return False
        else:
            return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()