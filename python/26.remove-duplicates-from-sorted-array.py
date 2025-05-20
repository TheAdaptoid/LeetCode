#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        occurrence = {}

        for num in nums:
            if num not in occurrence:
                occurrence[num] = 1
            else:
                occurrence[num] += 1

        for key in occurrence.keys():
            for times in range(occurrence[key] - 1):
                nums.remove(key)

        return len(nums)


# @lc code=end
