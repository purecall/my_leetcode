// 减治法
/* 两种选择
1.左下角：往右走增大，往上走减小
2.右上角：往下走增大，往左走减小

比如选了左上角，当target > nums[row][col]时，只能往右走，
因为上面所有的数都比当前数小，这一列就可以被排除了
*/
func searchMatrix(matrix [][]int, target int) bool {
	if len(matrix) == 0 {
		return false
	}
	col, row := 0, len(matrix)-1
	for row >= 0 && col <= len(matrix[0])-1 {
		if matrix[row][col] == target {
			return true
		} else if matrix[row][col] < target {
			col++
		} else {
			row--
		}
	}
	return false
}