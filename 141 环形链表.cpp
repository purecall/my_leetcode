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
		// 1. 暴力：遍历链表，hash/set
		//    遍历所有节点并用哈希表存储每个节点的地址，遍历链表并判断是否有节点已存在于哈希表中直到nullptr(尾部)

		// 2. 快慢指针(O(1)内存)
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
