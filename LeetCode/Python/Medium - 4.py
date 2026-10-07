class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        left_product = 1
        right_product = 1

        left = []
        right = []

        for i in range(len(nums)):
            left.append(left_product)
            left_product *= nums[i]
        
        for i in range(len(nums) - 1, -1, -1):
            right.append(right_product)
            right_product *= nums[i]
        
        answer = []

        for i in range(len(nums)):
            answer.append(left[i] * right[len(nums)-1-i])
        
        return answer
