class Solution {
public:
    int lengthOfLastWord(string s) {
        int ret = 0;
        int s_len = s.length() - 1;
        for (int i = s.length() - 1; i >= 0; i--) {
            if (s[i] == ' ') {
                s_len--;
                continue;
            }
            else {
                break;
            }
        }
        for (int i = s_len; i >= 0; i--) {
            if (s[i] == ' ') {
                return ret;
            }
            else {
                ret++;
            }
        }
        return ret;
    }
};