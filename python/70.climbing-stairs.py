#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        def factorial(n):
            if n == 0:
                return 1
            else:
                return n * factorial(n - 1)

        return int(factorial(n) / (factorial(n - 2)))


# @lc code=end
