#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        int_string: str = str(x)

        factor: int = 1
        if int_string.startswith("-"):
            int_string = int_string[1:]
            factor = -1

        rev_int: int = int(int_string[::-1])

        if rev_int > (2**31 - 1) or rev_int < (-2 * 31):
            return 0

        return rev_int * factor


# @lc code=end
