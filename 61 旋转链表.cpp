#include<iostream>


struct ListNode {
	int val;
	ListNode* next;
	ListNode(int x) : val(x), next(NULL) {}
};

// �ҵ�����ɵ�β��������������ͷ���� old_tail.next = head����ʱ����պϳɻ���ͬʱ���������ĳ���n
// �ҵ��µ�β������(n - k%n -1)���ڵ㣬�µ�����ͷ�ǵ�(n - k%n)���ڵ�
// �Ͽ��� new_tail.next = nullptr���������µ�����ͷ new_head
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