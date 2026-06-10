class MinStack:

    def __init__(self):
        self.minStack = []
        self.min_values = []
     
    def push(self, val: int) -> None:
        self.minStack.append(val)

        # Na segunda pilha precisa saber qual é o menor valor atual
        if self.min_values:
            val = min(val, self.min_values[-1])
            
        self.min_values.append(val)


    def pop(self) -> None:
        self.minStack.pop()
        self.min_values.pop()

    def top(self) -> int:
        if(self.minStack):
            return self.minStack[-1]
        
    def getMin(self) -> int:
        return self.min_values[-1]

        
