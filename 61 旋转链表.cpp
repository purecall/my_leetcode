#include<iostream>


struct ListNode {
	int val;
	ListNode* next;
	ListNode(int x) : val(x), next(NULL) {}
};

// 找到链表旧的尾部并将其与链表头相连 old_tail.next = head，此时链表闭合成环，同时计算出链表的长度n
// 找到新的尾部，第(n - k%n -1)个节点，新的链表头是第(n - k%n)个节点
// 断开环 new_tail.next = nullptr，并返回新的链表头 new_head
class Solution {
public:
	ListNode* rotateRight(ListNode* head, int k) {
		// bad cases
		if ((head == nullptr) || (head->next == nullptr))
			return head;

		// close the linked list into a ring
		ListNode* old_tail = head;
		int n;
		for (n = 1; old_tail->next != nullptr; n++) {
			old_tail = old_tail->next;
		}
		old_tail->next = head;

		// find new tail: (n - k%n -1)th node
		// find new head: (n - k%n)th node
		ListNode* new_tail = head;
		for (int i = 0; i < n - k % n - 1; i++) {
			new_tail = new_tail->next;
		}
		ListNode* new_head = new_tail->next;

		// break the ring
		new_tail->next = nullptr;

		return new_head;
	}
};