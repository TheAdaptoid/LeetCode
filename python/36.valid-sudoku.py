#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for rIndex in len(board):
            digits: list[str] = [x for x in board[rIndex] if x != "."]
            for digit in digits:
                if digits.count(digit) > 1:
                    return False

        # check columns


# @lc code=end
