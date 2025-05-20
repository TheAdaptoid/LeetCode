#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        for element in nums:
            if element in counts:
                counts[element] += 1
            else:
                counts[element] = 1

        return max(counts, key=counts.get)


# @lc code=end
