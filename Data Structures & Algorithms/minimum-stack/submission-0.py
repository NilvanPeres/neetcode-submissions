class MinStack:

    def __init__(self):
        self.minStack = []
     
    def push(self, val: int) -> None:
        self.minStack.append(val)

    def pop(self) -> None:
        if(self.minStack):
            self.minStack.pop()

    def top(self) -> int:
        if(self.minStack):
            return self.minStack[-1]
        
    def getMin(self) -> int:
        min_value = 2147483647

        if (self.minStack):
            print("Pilha: ", self.minStack)
            for i in range(len(self.minStack)):
                min_value = min(min_value, self.minStack[i])

            return min_value

        
