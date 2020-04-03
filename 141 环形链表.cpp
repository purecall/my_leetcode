#include<iostream>

using namespace std;

struct ListNode {
	int val;
	ListNode* next;
	ListNode(int x) :val(x), next(nullptr) {}
};

class Solution {
public:
	bool hasCycle(ListNode* head) {
		// 1. ��������������hash/set
		//    �������нڵ㲢�ù�ϣ��洢ÿ���ڵ�ĵ�ַ�����������ж��Ƿ��нڵ��Ѵ����ڹ�ϣ����ֱ��nullptr(β��)

		// 2. ����ָ��(O(1)�ڴ�)
		if (head == nullptr || head->next == nullptr) {
			return false;
		}

		ListNode* slow_ptr = head;
		ListNode* fast_ptr = head->next;

		while (slow_ptr != fast_ptr) {
			if (fast_ptr == nullptr || fast_ptr->next == nullptr) {
				return false;
			}
			slow_ptr = slow_ptr->next;
			fast_ptr = fast_ptr->next->next;
		}
	}
};
