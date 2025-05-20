#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        elif len(str(x)) % 2 == 0:
            left = str(x)[: int(len(str(x)) / 2)]
            right = str(x)[int(len(str(x)) / 2) :]

            right = right[::-1]

            if left == right:
                return True
            else:
                return False

        else:
            left = str(x)[: int(len(str(x)) / 2)]
            right = str(x)[int(len(str(x)) / 2) + 1 :]

            right = right[::-1]

            if left == right:
                return True
            else:
                return False


# @lc code=end
