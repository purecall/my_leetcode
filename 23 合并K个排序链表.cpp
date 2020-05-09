#include<iostream>
#include<vector>
using namespace std;

struct ListNode {
	int val;
	ListNode* next;
	ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
	// merge两个有序链表
	ListNode* merge(ListNode* p1, ListNode* p2) {
		if (!p1)
			return p2;
		if (!p2)
			return p1;

		if (p1->val <= p2->val) {
			p1->next = merge(p1->next, p2);
			return p1;
		}
		else {
			p2->next = merge(p1, p2->next);
			return p2;
		}
	}

	// 将一个链表vector用分治的方法merge
	ListNode* merge(vector<ListNode*>& lists, int start, int end) {
		if (start == end)
			return lists[start];

		int mid = (start + end) / 2;
		ListNode* l1 = merge(lists, start, mid);
		ListNode* l2 = merge(lists, mid + 1, end);
		return merge(l1, l2);
	}

	ListNode* mergeKLists(vector<ListNode*>& lists) {
		if (lists.size() == 0) {
			return nullptr;
		}
		return merge(lists, 0, lists.size() - 1);
	}
};