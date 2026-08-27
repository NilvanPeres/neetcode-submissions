import random

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:


        def calculate(values: List[int]) -> int:
            return values[0] ** 2 + values[1] ** 2

        def quickSelect(s: int, e: int):

            #Base case
            if ((e - s) + 1 <= 1):
                return

            #pivot
            pivot_idx = random.randint(s, e)

            # Swap
            points[e], points[pivot_idx] = points[pivot_idx], points[e]

            pivot = points[e]

            #Pointeiro
            left = s

            for i in range(s, e):
                if (calculate(points[i]) < calculate(pivot)):
                    tmp = points[left]
                    points[left] = points[i]
                    points[i] = tmp
                    left += 1

            # Swap de pivot para posição ordenada
            points[e], points[left] = points[left], pivot 

            # Quick select. Só chama recursivamente para onde precisa:
            if (left == k):
                return
            elif(left < k):
                quickSelect(left+1, e)
            else:
                quickSelect(s, left-1)

        quickSelect(0, len(points)- 1)

        return points[:k]
        