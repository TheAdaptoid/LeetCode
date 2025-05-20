#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def Get_Next_Index(index: int) -> int:
            return (index + k) % len(nums)

        placeHolder: int = None

        # first step
        placeHolder = nums[k]
        nums[k] = nums[0]
        nums[0] = None

        index: int = k
        while placeHolder != None:
            nums[0] = nums[Get_Next_Index(index + k)]
            nums[Get_Next_Index(index + k)] = placeHolder
            placeHolder = nums[0]
            nums[0] = None

            index += k


# @lc code=end
