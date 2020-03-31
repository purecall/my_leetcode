#include<iostream>

using namespace std;

struct ListNode {
	int val;
	ListNode* next;
	ListNode(int x) :val(x), next(nullptr) {}
};

class Solution {
public:
	ListNode* reverseList(ListNode* head) {
		/*
			1. ˫ָ�룬һ��ʼ preΪNULL��curΪhead��Ȼ�󲻶ϱ���cur
			2. ÿ�ε�����cur������cur��nextָ��pre��Ȼ��pre��curǰ��һλ
			3. ���������֮��(cur==NULL)��pre�������һ���ڵ���
		*/
		ListNode* pre = nullptr;
		ListNode* cur = head;
		ListNode* tmp = nullptr;

		while (cur) {
			tmp = cur->next;	//��¼cur��next�ڵ�

			// ʹ��ǰ�ڵ�ָ��pre
			cur->next = pre;

			// pre��cur��ǰ��һλ
			pre = cur;
			cur = tmp;
		}
		return pre;
	}
};
