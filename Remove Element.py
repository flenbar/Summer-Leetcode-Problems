class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        n = len(nums)
        for fast in range(n):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow
