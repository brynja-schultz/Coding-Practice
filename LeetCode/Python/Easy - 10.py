class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        right_1 = m - 1
        right_2 = n - 1

        curr_index = len(nums1) - 1

        while right_2 >= 0:
            if right_1 < 0 or nums2[right_2] >= nums1[right_1]:
                nums1[curr_index] = nums2[right_2]
                right_2 -= 1
            else:
                nums1[curr_index] = nums1[right_1]
                right_1 -= 1
            curr_index -= 1
