#
# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#

# @lc code=start


class Term:
    def __init__(
        self, term: int | str, left: "Term" | None = None, right: "Term" | None = None
    ) -> None:
        self.term = term
        self.left = left
        self.right = right


class Solution:
    def calculate(self, s: str) -> int:
        operators: set[str] = {"+", "-", "(", ")"}
        prev_term: Term | None = None

        for idx, char in enumerate(s):
            # Skip spaces
            if char == " ":
                continue

            # Handle operators
            if char in operators:
                pass

            # Handle numbers
            number: int = int(char)
            term: Term = Term(number)

            # Clean up
            # If there was a term already
            # processed, become a child
            if prev_term:
                if prev_term.left:
                    prev_term.right = term
                else:
                    prev_term.left = term

        return 0


# @lc code=end
