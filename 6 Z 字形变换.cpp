#include<iostream>
#include<string>
#include<vector>
using namespace std;

class Solution {
public:
	string convert(string s, int numRows) {
		if (numRows == 1) return s;

		vector<string> rows(min(numRows, int(s.length())));
		//���ǿ���ʹ�� min(numRows, len(s)) ���б�����ʾ Z ����ͼ���еķǿ���

		//�����ҵ��� s����ÿ���ַ���ӵ����ʵ��С�����ʹ�õ�ǰ�к͵�ǰ���������������Ժ��ʵ��н��и��١�
		//ֻ�е����������ƶ�����������л������ƶ������������ʱ����ǰ����Żᷢ���ı䡣

		int curRow = 0;
		bool goingDown = false;

		for (char c : s) {
			rows[curRow] += c;
			if (curRow == 0 || curRow == numRows - 1) goingDown = !goingDown;
			curRow += goingDown ? 1 : -1;
			// ����Ͳ��ÿ�����Z���ˣ�����һ��ssswwwsss����������ֻҪ����curRow�Ϳ����ˡ�
			// ֻ���ַ�����׷���ַ����հ׺���
		}

		string ret;
		for (string row : rows) ret += row;
		return ret;
	}
};