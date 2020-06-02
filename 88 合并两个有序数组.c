void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n) {
    int last = m + n - 1;
    while (n) {
        if (m == 0) {
            nums1[last--] = nums2[--n];
        }
        else if (nums2[n - 1] >= nums1[m - 1]) {
            nums1[last--] = nums2[--n];
        }
        else {
            nums1[last--] = nums1[--m];
        }
    }
}