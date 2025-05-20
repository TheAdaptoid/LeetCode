#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        nums = [x for x in nums if x >= 0]
        nums = sorted(nums)

        # empty lists
        if len(nums) == 0:
            return 1

        if nums[0] != 1 and nums[0] > 1:
            return 1

        for index in range(len(nums)):
            currentValue = nums[index]

            # only negatives
            if currentValue < 0:
                continue

            # only positives
            if currentValue >= 0 and len(nums) > index + 1:
                nextValue = nums[index + 1]

                if nextValue == currentValue:
                    continue

                if nextValue != currentValue + 1 or nextValue == currentValue:
                    return currentValue + 1

            else:
                return currentValue + 1

        # only negatives
        return 1


# @lc code=end
