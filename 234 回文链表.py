#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None or head.next == None:
            return True
        if head.next.next == None:
            return head.val == head.next.val

        # 快慢指针找中间节点
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # 反转后半边的链表
        # 如果长度为奇数2k+1，会产生2条长度均为k+1的链表
        # 如果长度为偶数2k，会产生2条长度均为k的链表
        fast = self.reverse(slow)  # 用fast暂存

        # 比较fast和head两个链表，
        while fast:
            if fast.val != head.val:
                return False
            fast = fast.next
            head = head.next
        return True

    def reverse(self, head):
        if head == None or head.next == None:
            return head
        
        pre = None
        cur = head
        tmp = None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

# @lc code=end
