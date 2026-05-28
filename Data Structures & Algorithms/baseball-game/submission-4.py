class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ''' 1. Iterar sobre a lista
            2. Precisa de um novo array que será manipulado de acordo com cada elemento '''

        new_array = []
        sum = 0
        for i in range(len(operations)):

            match operations[i]:
                case "+": 
                    print(new_array) 
                    new_array.append((new_array[len(new_array) -2]) + (new_array[len(new_array) - 1]))

                    sum += new_array[-1]

                case "C":
                    sum -= new_array[-1]
                    new_array.pop() 

                case "D":
                    value = new_array.pop()
                    multiplied_value = value * 2
                    new_array.extend([value, multiplied_value])
                    sum += new_array[-1]

                case _:
                    new_array.append(int(operations[i]))
                    sum += new_array[-1]
                    print(sum)

        return sum
        