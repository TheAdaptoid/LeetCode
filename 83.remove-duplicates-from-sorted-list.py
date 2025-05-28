#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class ListNode:
    def __init__(self, val=0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        # Start with the head
        prev_node: ListNode = head

        # Create a set with the head's value
        prev_values: set[int] = {head.val}

        # Begin iterating
        # with the 2nd node
        curr_node = head.next

        while curr_node:
            # If the value had not been seen
            # add the node to the list
            if curr_node.val not in prev_values:
                # add the value to the set
                prev_values.add(curr_node.val)

                # point to the non-duplicate
                prev_node.next = curr_node

                # push the node to the "queue"
                prev_node = curr_node

            # Get the next node
            curr_node = curr_node.next

        # Ensure the last node
        # points to nothing
        prev_node.next = None

        return head


# @lc code=end
