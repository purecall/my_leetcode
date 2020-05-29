#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

bool isNumber(char* s) {
	bool bIsNum = false;

	// 去除空格
	while (' ' == *s) {
		s++;
	}

	// 允许出现一个符号
	if ('-' == *s || '+' == *s) {
		s++;
	}

	// 整数部分
	while (isdigit(*s)) {
		bIsNum = true;
		s++;
	}

	// 允许出现一个小数点
	if ('.' == *s) {
		s++;
	}

	// 小数部分
	while (isdigit(*s)) {
		bIsNum = true;
		s++;
	}

	// 允许出现科学计数法，其前必须为数字
	if (bIsNum == true && 'e' == *s) {
		s++;
		bIsNum = false;

		// 幂次方允许出现一个符号
		if ('+' == *s || '-' == *s) {
			s++;
		}

		// 幂次方部分
		while (isdigit(*s)) {
			s++;
			bIsNum = true;
		}
	}

	while (' ' == *s) {
		s++;
	}

	// 判断是否已经到了字符串末尾
	return ('\0' == *s && bIsNum);
}
