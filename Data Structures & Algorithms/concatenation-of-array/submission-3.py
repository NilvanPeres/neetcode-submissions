class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ''' 1. Precisa criar um novo array, e seu tamanho deve ser 2x maior que o anterior
            2. O novo array vai ter todos elementos válidos do array antigo
            3. O novo array vai começar a repetir a partir do index 0 os valores do antigo array
         '''
        size_old_array = len(nums) 
        size_new_array = 2 * size_old_array
        new_array = [0] * size_new_array 

        # Minha solução
        # for i in range(len(new_array)):
        #     # Copy values ans[i] == nums[i]
        #     if (i < size_old_array):
        #         new_array[i] = nums[i]
        #     else:
        #         new_array[i] = nums[i - size_old_array]

        # Solução um pouco melhor abaixo. Usa uma constante menor e não há condicionais,
        # aproveita a lógica do tamanho do array antigo

        for i in range(len(nums)):
            new_array[i] = nums[i]
            new_array[i + size_old_array] = nums[i]

        return new_array

        # Solução roubada dificilmente em uma entrevista pano deixariam usar isso
        # return nums + nums