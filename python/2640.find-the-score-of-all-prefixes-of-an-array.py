#
# @lc app=leetcode id=2640 lang=python3
#
# [2640] Find the Score of All Prefixes of an Array
#

# @lc code=start
class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        n: int = len(nums)
        max_array: list[int] = [0] * n
        max_array[0] = nums[0]  # the first element will always be the same

        # max_array[i] = max(
        #     the current element,
        #     the largest element previously observed
        # )
        for index in range(1, n):
            max_array[index] = max(max_array[index - 1], nums[index])

        # c[i] = nums[i] + max_array[i]
        conversion: list[int] = [nums[i] + max_array[i] for i in range(n)]

        conversion_sums: list[int] = [0] * n
        conversion_sums[0] = conversion[0]  # the first element will always be the same
        for index in range(1, n):
            # the current index is equal to the value at the
            # same index in the conversion array plus the
            # previous index in the conversion_sums array
            conversion_sums[index] = conversion[index] + conversion_sums[index - 1]

        return conversion_sums


# @lc code=end
