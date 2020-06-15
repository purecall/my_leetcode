#include<iostream>
#include<string>
#include<vector>
using namespace std;

class Solution {
public:
	string convert(string s, int numRows) {
		if (numRows == 1) return s;

		vector<string> rows(min(numRows, int(s.length())));
		//我们可以使用 min(numRows, len(s)) 个列表来表示 Z 字形图案中的非空行

		//从左到右迭代 s，将每个字符添加到合适的行。可以使用当前行和当前方向这两个变量对合适的行进行跟踪。
		//只有当我们向上移动到最上面的行或向下移动到最下面的行时，当前方向才会发生改变。

		int curRow = 0;
		bool goingDown = false;

		for (char c : s) {
			rows[curRow] += c;
			if (curRow == 0 || curRow == numRows - 1) goingDown = !goingDown;
			curRow += goingDown ? 1 : -1;
			// 这里就不用考虑走Z型了，就是一个ssswwwsss操作，所以只要考虑curRow就可以了。
			// 只往字符串上追加字符，空白忽略
		}

		string ret;
		for (string row : rows) ret += row;
		return ret;
	}
};