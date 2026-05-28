class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ''' 1. Precisa criar um novo array, e seu tamanho deve ser 2x maior que o anterior
            2. O novo array vai ter todos elementos válidos do array antigo
            3. O novo array vai começar a repetir a partir do index 0 os valores do antigo array
         '''
        # size_old_array = len(nums) 
        # size_new_array = 2 * size_old_array
        # new_array = [0] * size_new_array 

        # for i in range(len(new_array)):
        #     # Copy values ans[i] == nums[i]
        #     if (i < size_old_array):
        #         new_array[i] = nums[i]
        #     else:
        #         new_array[i] = nums[i - size_old_array]

        # return new_array

        return nums + nums