#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_leaf(self, node: TreeNode) -> bool:
        # If children are present
        # then not a leaf
        if node.left or node.right:
            return False
        return True

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # If the root is none
        # then skip it
        if root is None:
            return 0

        # If the root is a leaf,
        # then skip it
        if self.is_leaf(root):
            return 0

        left_sum: int = 0
        right_sum: int = 0

        # Check the left node
        if root.left:
            # If the left node is a leaf
            # then save it's value
            if self.is_leaf(root.left):
                left_sum += root.left.val
            # Otherwise, recurse the left node
            else:
                left_sum += self.sumOfLeftLeaves(root.left)

        # Check the right node
        if root.right:
            # If the right node is a not leaf
            # then recurse it
            if not self.is_leaf(root.right):
                right_sum += self.sumOfLeftLeaves(root.right)

        return left_sum + right_sum


# @lc code=end
