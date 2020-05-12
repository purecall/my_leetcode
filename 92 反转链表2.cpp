#include<iostream>

struct ListNode {
	int val;
	ListNode* next;
	ListNode(int x) : val(x), next(NULL) {}
};

// ���跴ת��λ�� m-n
// pre   ->  m-1
// start ->  m
// end   ->  n
// next  ->  n+1
// ��תstart-end����ƴ��
// ��� m == 1���Ͳ�����pre


class Solution {
public:
	ListNode* reverse(ListNode* head) {
		ListNode* pre = nullptr;
		ListNode* cur = head;
		ListNode* tmp = nullptr;

		while (cur) {
			tmp = cur->next;
			cur->next = pre;
			pre = cur;
			cur = tmp;
		}
		return pre;
	}

	ListNode* reverseBetween(ListNode* head, int m, int n) {
		ListNode* pre = head;
		ListNode* start = head;
		ListNode* end = head;
		ListNode* next = head;
		// m==1�Ͳ�����pre
		if (m == 1) {
			pre = nullptr;
		}
		else if (m > 1) {
			for (int i = 0; i < m - 2; i++) {
				pre = pre->next;
			}
			start = pre->next;
		}

		for (int i = 0; i < n - 1; i++) {
			end = end->next;
		}

		next = end->next; // �����Ƿ����

		// �Ͽ�
		if (m > 1) {
			pre->next = nullptr;
		}
		end->next = nullptr;

		end = start; // �м�һ�η�ת�����ڵ�start���Ǻ����end
		start = reverse(start);

		if (m > 1) {
			pre->next = start;
		}
		else if (m == 1) {
			head = start;
		}
		end->next = next;
		return head;
	}
};