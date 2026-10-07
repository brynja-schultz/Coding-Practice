class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        curr_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            max_sum = max(max_sum + nums[i], nums[i])
            curr_sum = max(curr_sum, max_sum)

        return curr_sum
