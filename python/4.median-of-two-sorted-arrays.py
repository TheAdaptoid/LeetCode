#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Combine two sorted arrays into one
        nums = sorted(nums1 + nums2)

        # Find the median
        if len(nums) % 2 == 0:
            leftValue = nums[int(len(nums) / 2 - 1)]
            rightValue = nums[int(len(nums) / 2)]

            return (leftValue + rightValue) / 2
        else:
            index = (len(nums) / 2) - 0.5
            return nums[int(index)]


# @lc code=end
