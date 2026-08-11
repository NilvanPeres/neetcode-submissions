class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # Must return nums1 as merged and sorted array

        nums1_copy = nums1[: m] # cópia até o elemento válido

        # Três ponteiros: i, j, k (um para percorrer nums1_copy, outro para nums2 e outro per nums1 as result)
        i, j, k = 0, 0, 0

        while (i < m and j < n):
            if (nums1_copy[i] < nums2[j]):
                nums1[k] = nums1_copy[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1
        
        while (i < m):
            nums1[k] = nums1_copy[i]
            k += 1
            i += 1

        while (j < n):
            nums1[k] = nums2[j]
            k += 1
            j += 1
        

