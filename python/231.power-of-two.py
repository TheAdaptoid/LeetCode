#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if (2 ** (n.bit_length() - 1)) == n:
            return True
        return False


# @lc code=end
