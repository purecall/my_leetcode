#include<iostream>

struct ListNode {
	int val;
	ListNode* next;
	ListNode(int x) : val(x), next(NULL) {}
};

// 假设反转的位置 m-n
// pre   ->  m-1
// start ->  m
// end   ->  n
// next  ->  n+1
// 反转start-end，再拼接
// 如果 m == 1，就不存在pre


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
		// m==1就不存在pre
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

		next = end->next; // 无论是否存在

		// 断开
		if (m > 1) {
			pre->next = nullptr;
		}
		end->next = nullptr;

		end = start; // 中间一段反转后，现在的start就是后面的end
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