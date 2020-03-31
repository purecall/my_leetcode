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
			1. 双指针，一开始 pre为NULL，cur为head，然后不断遍历cur
			2. 每次迭代到cur，都将cur的next指向pre，然后pre和cur前进一位
			3. 都迭代完成之后(cur==NULL)，pre就是最后一个节点了
		*/
		ListNode* pre = nullptr;
		ListNode* cur = head;
		ListNode* tmp = nullptr;

		while (cur) {
			tmp = cur->next;	//记录cur的next节点

			// 使当前节点指向pre
			cur->next = pre;

			// pre和cur都前进一位
			pre = cur;
			cur = tmp;
		}
		return pre;
	}
};
