#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        braceSet = list(s)

        for brace in braceSet:
            if brace == "(" or brace == "[" or brace == "{":
                stack.append(brace)

            elif brace == ")" and len(stack) > 0 and stack[-1] == "(":
                stack.pop()
            elif brace == "]" and len(stack) > 0 and stack[-1] == "[":
                stack.pop()
            elif brace == "}" and len(stack) > 0 and stack[-1] == "{":
                stack.pop()
            else:
                return False

        return len(stack) == 0


# @lc code=end
