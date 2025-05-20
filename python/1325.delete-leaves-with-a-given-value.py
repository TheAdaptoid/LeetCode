#
# @lc app=leetcode id=1325 lang=python3
#
# [1325] Delete Leaves With a Given Value
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def removeLeafNodes(
        self, root: Optional[TreeNode], target: int
    ) -> Optional[TreeNode]:
        def remove_target(root, target: int):
            # If the root is empty, return
            if root is None:
                return None

            # Check children
            root.left = remove_target(root.left, target)
            root.right = remove_target(root.right, target)

            # If either child still exists
            # then the root is not a leaf,
            # return the un-deleted root
            if root.left or root.right:
                return root

            # Otherwise, delete the root
            if root.val == target:
                return None

            # If the root's value is not the target
            # return the root as is
            return root

        return remove_target(root=root, target=target)


# @lc code=end
