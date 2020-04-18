package my_leetcode

func findMin(nums []int) int {
	left, right := 0, len(nums)-1
	for left <= right {
		// 事实上不会跳出循环，当left==mid时直接返回
		if nums[left] <= nums[right] { // 如果[left,right]递增，直接返回
			return nums[left]
		}
		mid := left + (right-left)/2
		if nums[left] <= nums[mid] { // [left,mid]递增，则到[mid+1,right]中寻找
			left = mid + 1
		} else {
			right = mid // [left,mid]不连续，在[left,mid]中查找
			// 注意，是 mid 而不是 mid+1 ，因为无法排除当前mid
		}
	}
	return -1
}
