// 查找或插入一个长度为 L 的单词，访问 next 数组的次数最多为 L+1，和 Trie 中包含多少个单词无关。
class Trie {
private:
	bool isEnd; // 该节点是否是一个串的结束
	Trie* next[26]; // 字母映射表

public:
	Trie() {
		isEnd = false;
		memset(this->next, 0, sizeof(this->next));
	}

	// 插入
	void insert(string word) {
		Trie* node = this;
		for (char c : word) {
			if (node->next[c - 'a'] == nullptr) {
				node->next[c - 'a'] = new Trie();
			}
			node = node->next[c - 'a'];
		}
		node->isEnd = true;
	}

	// 查找
	bool search(string word) {
		Trie* node = this;
		for (char c : word) {
			node = node->next[c - 'a'];
			if (node == nullptr) {
				return false;
			}
		}
		return node->isEnd;
	}

	// 前缀匹配
	bool startsWith(string prefix) {
		Trie* node = this;
		for (char c : prefix) {
			node = node->next[c - 'a'];
			if (node == nullptr) {
				return false;
			}
		}
		return true;
	}
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */