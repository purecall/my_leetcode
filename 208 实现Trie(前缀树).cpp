// ���һ����һ������Ϊ L �ĵ��ʣ����� next ����Ĵ������Ϊ L+1���� Trie �а������ٸ������޹ء�
class Trie {
private:
	bool isEnd; // �ýڵ��Ƿ���һ�����Ľ���
	Trie* next[26]; // ��ĸӳ���

public:
	Trie() {
		isEnd = false;
		memset(this->next, 0, sizeof(this->next));
	}

	// ����
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

	// ����
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

	// ǰ׺ƥ��
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