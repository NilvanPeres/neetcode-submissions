class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # M == len(nums1)
        # N == len(nums2)
        # Must return nums1 ordered and merged with nums2 --> in-place alterações

        # Copy nums1
        copy_nums_1 = nums1[: m]

        # Pointers 
        i, j, k = 0, 0, 0

        while (i < m and j < n):
            if (copy_nums_1[i] < nums2[j]):
                nums1[k] = copy_nums_1[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1

            k += 1


        # Resto da lista caso tenha elementos...
        while (i < m) :
            nums1[k] = copy_nums_1[i]
            i += 1
            k += 1

        while (j < n) :
            nums1[k] = nums2[j]
            j += 1
            k += 1

