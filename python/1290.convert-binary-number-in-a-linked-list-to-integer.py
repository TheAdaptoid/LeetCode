#
# @lc app=leetcode id=1290 lang=python3
#
# [1290] Convert Binary Number in a Linked List to Integer
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        c_node = head
        binary: int = 0
        while c_node is not None:
            binary = (binary * 10) + c_node.val
            c_node = c_node.next

        return int(str(binary), base=2)


# @lc code=end
