class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        # Vou precisar de 2 loops. Um na posição atual e outro para ir comparando com os vizinhos
        # Uma variável para guardar max_value

        # for i in range(len(arr)):
        #     max_value = 0
        #     for j in range(i + 1, len(arr)):
        #         if (arr[j] > max_value):
        #             max_value = arr[j]
        #     arr[i] = max_value

        # arr[-1] = -1

        max_value = -1

        for i in range(len(arr) -1, -1, -1):
            new_max = max(max_value, arr[i])
            arr[i] = max_value
            max_value = new_max

        return arr

        
 

        

        