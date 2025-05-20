#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern) != len(s.split(" ")):
            return False

        charMap: dict[str, str] = {}
        for char in pattern:
            charMap[char] = ""

        for word in s.split(" "):
            for char, value in charMap.items():
                if value == "":
                    charMap[char] = word
                    break
                else:
                    if charMap[char] == word:
                        continue

        baseString: list[str] = []
        for char in pattern:
            baseString.append(charMap[char])

        if baseString == s.split(" "):
            return True
        else:
            return False


# @lc code=end
