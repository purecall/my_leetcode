#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
class Solution {
public:
	uint32_t reverseBits(uint32_t n) {
		uint32_t ret = 0;
		for (int power = 31; n != 0; n >>= 1, power--) {
			ret += (n & 1) << power;
		}
		return ret;
	}
};