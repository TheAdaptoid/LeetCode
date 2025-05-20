#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        currLength = 0
        prevChars: dict[str, int] = {}

        for char in list(s):
            if char in prevChars:
                return self.lengthOfLongestSubstring(s=s[prevChars[char] + 1 :])

            currLength += 1
            prevChars[char] = list(s).index(char)
            maxLength = max(maxLength, currLength)

        return maxLength


# @lc code=end
