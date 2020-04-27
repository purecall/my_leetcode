package main

type Trie struct {
	children [26]*Trie
	isEnd    bool
}

func Constructor() Trie {
	return Trie{}
}

func (this *Trie) Insert(word string) {
	node := this
	for _, char := range word {
		index := char - 'a'
		if node.children[index] == nil {
			trie := Constructor()
			node.children[index] = &trie
		}
		node = node.children[index]
	}
	node.isEnd = true
}

func (this *Trie) Search(word string) bool {
	node := this
	for _, char := range word {
		index := char - 'a'
		node = node.children[index]
		if node == nil {
			return false
		}
	}
	return node.isEnd
}

func (this *Trie) StartsWith(prefix string) bool {
	node := this
	for _, char := range prefix {
		index := char - 'a'
		node = node.children[index]
		if node == nil {
			return false
		}
	}
	return true
}
