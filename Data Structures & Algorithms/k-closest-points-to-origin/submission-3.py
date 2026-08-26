import random

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # Calcular distancia
        def calculate_distance(point: List[int]) -> int:
            return point[0] ** 2 + point[1] ** 2

        # Base case - parada
        s: int = 0
        e: int = len(points) - 1

        def quickSelect(s: int, e: int):

            if (e - s) + 1 <= 1:
                return

            # Pivot
            pivot_idx = random.randint(s, e)
            points[pivot_idx], points[e] = points[e], points[pivot_idx]
            pivot_dist = calculate_distance(points[e])

            # ponteiro
            left = s

            for i in range(s, e):
                if (calculate_distance(points[i]) < pivot_dist):
                    tmp = points[left]
                    points[left] = points[i]
                    points[i] = tmp
                    left += 1

            # Atualiza posição do pivot
            points[e], points[left] = points[left], points[e]

            #Quickselect -> só vai recursivamente para onde precisa

            if (left == k):
                return
            elif (left < k):
                quickSelect(left + 1, e)
            else:
                quickSelect(s, left-1)

        quickSelect(0, len(points) -1)

        return points[:k]

            

        

        
        