#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        charSet = ""

        for char in strs[0]:
            valid = True
            for word in strs:
                valid = word.startswith(charSet + char)

                if not valid:
                    break

            if valid:
                charSet += char

        return charSet


# @lc code=end
