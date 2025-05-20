#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Start at the end
        current_index: int = len(digits) - 1

        carry: bool = True
        while carry:
            # Add a new leading digit
            if current_index == -1:
                # Create a new array
                new_size: int = len(digits) + 1
                new_digits: list[int] = [1] * new_size

                # copy digits
                for index in range(new_size - 1):
                    new_digits[index + 1] = digits[index]

                # return the new digit array
                return new_digits

            # Increment value
            if digits[current_index] == 9:
                digits[current_index] = 0
                carry = True
                current_index -= 1  # Efficient eval
            else:
                digits[current_index] += 1
                carry = False

        # Return the given digit array
        return digits


# @lc code=end
