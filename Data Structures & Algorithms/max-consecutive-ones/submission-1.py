class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    #    # Precisa ocorrer de forma consecutiva...
    #    # Passos do algoritmo:
    #    # 1. Iterar sobre o array 
    #    # 2. Ter um int para guardar o máximo
    #    # 3. quando for encerrado o sum, vai iniciar um novo possível contador e preciso comparar para substituir
        maxConcurrencyValue = 0
        auxValuecount = 0
        for i in range(len(nums)):
            if (nums[i] == 1): # começa a contagem
                auxValuecount += 1
                if (maxConcurrencyValue < auxValuecount): # atualiza valor apenas se nova sequencia for maior
                    maxConcurrencyValue = auxValuecount
            else: #reseta o valor da aux
                auxValuecount = 0

        return maxConcurrencyValue

    # def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    #     max_count = 0
    #     current_count = 0
        
    #     for num in nums:
    #         if num == 1:
    #             current_count += 1
    #             max_count = max(current_count, max_count)
    #         else:
    #             current_count = 0
        
    #     return max_count



     
        