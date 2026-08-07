class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # m = number of valids elements in nums1
        # n = number of valids in nums2
        i, j, k = 0, 0, 0

        copy_nums1 = nums1[0: m+1]

        while (i < m and j < n):
            if (copy_nums1[i] < nums2[j]):
                print("Qual o valor de copy_nums1[i]: ", nums1[i])
                #print("Onde esta copy1: ", copy_nums1[i])
                nums1[k] = copy_nums1[i]
                i += 1

            else:
                print("Qual o valor de nums2[j]: ", nums2[j])
                nums1[k] = nums2[j]
                j += 1

            # print("Valor do k: ", nums1[k])
            # print("Indice do K: ", k)
            k += 1

        # resto do que sobrou
        while (i < m):
            nums1[k] = copy_nums1[i]
            i += 1
            k += 1

        while(j < n):
            nums1[k] = nums2[j]
            j += 1
            k += 1