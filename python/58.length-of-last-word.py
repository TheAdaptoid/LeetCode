#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split(" ")

        while words[-1] == "":
            words.pop()

        return len(words[-1])


# @lc code=end
