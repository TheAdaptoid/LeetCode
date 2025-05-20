#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        marks = list(s)
        marks.append(0)

        total = 0
        for index in range(len(marks)):
            if marks[index] == "I":
                if marks[index + 1] == "V" or marks[index + 1] == "X":
                    total -= 1
                else:
                    total += 1

            elif marks[index] == "X":
                if marks[index + 1] == "L" or marks[index + 1] == "C":
                    total -= 10
                else:
                    total += 10

            elif marks[index] == "C":
                if marks[index + 1] == "D" or marks[index + 1] == "M":
                    total -= 100
                else:
                    total += 100

            elif marks[index] == "V":
                total += 5
            elif marks[index] == "L":
                total += 50
            elif marks[index] == "D":
                total += 500
            elif marks[index] == "M":
                total += 1000

            elif marks[index] == 0:
                break

        return total


# @lc code=end
