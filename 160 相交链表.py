#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # listA 作为一个集合，再去遍历listB
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        A = set()
        curA = headA
        curB = headB
        while curA:
            A.add(curA)
            curA = curA.next
        while curB:
            if curB in A:
                return curB
            curB = curB.next
        return None


# @lc code=end

class Solution1:
    # a_first + rest + b_first = b_first + rest + a_first
    # 相遇的时候就是第一个公共节点
    # 如果没有公共节点，最后None==None退出
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        curA, curB = headA, headB
        while curA != curB:
            curA = curA.next if curA else headB
            curB = curB.next if curB else headA
        return curA 