class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        initials = 0
        suma = n + m
        for i in range(m,suma):
            nums1[i] = nums2[initials]
            initials += 1
        nums1.sort()    

        
