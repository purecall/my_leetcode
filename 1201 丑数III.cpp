class Solution {
public:
	long gcd(long a, long b) {
		return a % b == 0 ? b : gcd(b, a % b);
	}

	// 最小公倍数
	long lcm(long a, long b) {
		return a / gcd(a, b) * b;
	}

	int nthUglyNumber(int n, int a, int b, int c) {
		long ab = lcm(a, b);
		long ac = lcm(a, c);
		long bc = lcm(b, c);
		long abc = lcm(ab, c);
		long left = 0;
		long right = 2e9;

		while (left <= right) {
			long mid = left + (right - left) / 2;
			int count = mid / a + mid / b + mid / c - mid / ab - mid / ac - mid / bc + mid / abc;
			if (count >= n) {
				right = mid - 1;
			}
			else {
				left = mid + 1;
			}
		}
		return left;
	}
};