#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        def Read(node: ListNode) -> int:
            number: str = ""
            while node:
                number = str(node.val) + number
                node = node.next

            return int(number)

        def Write(number: int) -> ListNode:
            prevNode = None
            for digit in str(number):
                node = ListNode(int(digit), prevNode)
                prevNode = node

            return prevNode

        return Write(Read(l1) + Read(l2))


# @lc code=end
