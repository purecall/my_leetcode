#include <string.h>
class Solution {
public:
    int countPrimes(int n) {
        auto isPrime = new bool[n];
        memset(isPrime, true, n);
        for (int i = 2; i * i < n; i++) {
            if (isPrime[i]) {
                for (int j = 2 * i; j < n; j += i) {
                    // 这里可以优化 j = i*i 开始，没想明白
                    isPrime[j] = false;
                }
            }
        }

        int count = 0;
        for (int i = 2; i < n; i++) {
            if (isPrime[i]) {
                count += 1;
            }
        }
        return count;
    }
};