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

    def addTwoNumbers2(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # create a new linked list to store sum
        res = ListNode(0)
        curr_node = res

        # init current sum and complement
        s, c = 0, 0

        # 1,2,3
        # 1,8
        # 2,0,4

        # iterate through linked lists
        while l1 or l2 or c > 0:
            l1_value = l1.val if l1 else 0
            l2_value = l2.val if l2 else 0

            current_value = l1_value + l2_value + c
            new_node = ListNode(current_value % 10)
            c = current_value // 10  # store complement

            curr_node.next = new_node
            curr_node = new_node

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return res.next
