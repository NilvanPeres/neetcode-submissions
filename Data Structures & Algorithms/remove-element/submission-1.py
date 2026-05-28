class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # 1. Mudar o array para que os primeiros elementos sejam os valores que são diferentes de 'VAL'
        # 2. Retornar quantidade de valores diferente de 'val'
        
        count_differents = 0
        i = 0
        j = len(nums) -1

        while (i <= j):
            if nums[i] != val:
                count_differents += 1
                i +=1
            else: 
                nums[i] = nums[j]
                j -= 1
            

        return count_differents
        