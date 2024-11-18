"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # create a new linked list to store sum
        sum_ll = ListNode()
        head = sum_ll

        # init current sum and complement
        s, c = 0, 0

        # 1,2,3
        # 1,8
        # 2,0,4

        # iterate through linked lists
        while l1 or l2 or c > 0:
            if l1:
                s += l1.val
                l1 = l1.next

            if l2:
                s += l2.val
                l2 = l2.next

            sum_ll.val = (s + c) % 10
            c = (s + c) // 10  # store complement

            if l1 or l2 or c > 0:
                sum_ll.next = ListNode()
                sum_ll = sum_ll.next

            print(s, c)

            s = 0  # reset current sum

        return head
