class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # size off array nums1 is equal to: m+n

        ''' 
            1. Create a copy of nums1 // maybe not necessary
            2. Gonna use 3 index -> iterate thought nums1copy nums2 and rewrite on nums1
        '''  

        length_of_n1 = m+n
        
        i, j, k = 0, 0, 0

        # copy
        copy_nums_1 = nums1[0 : m]

        print("copy: ", copy_nums_1)

        while (i < len(copy_nums_1) and j < len(nums2)):
           
            # Se for menor, troca
            if (copy_nums_1[i] > nums2[j]):
                nums1[k] = nums2[j]
                j += 1
            else :
                print("elem de copy: ", copy_nums_1[i])
                nums1[k] = copy_nums_1[i]
                i +=1

            k += 1


        print("nums1 before last two whiles: ", nums1)
        while (i < len(copy_nums_1)):
            nums1[k] = copy_nums_1[i]
            i +=1
            k +=1

        while (j < len(nums2)):
            nums1[k] = nums2[j]
            j += 1
            k += 1
        

        