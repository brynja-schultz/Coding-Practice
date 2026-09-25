class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        curr = 0
        for idx in range(len(nums)):
            if nums[idx] != 0:
                nums[curr] = nums[idx]
                curr += 1
                
        for i in range(curr, len(nums)):
            nums[i] = 0
