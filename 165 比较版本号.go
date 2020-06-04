import "strings"
// 1. 对两个版本号进行切割，得到两份版本数组
// 2. 补全两份版本数组到一样的长度，短的后面补0
// 3. 比较版本数组中每一个版本的大小
func compareVersion(version1 string, version2 string) int {
	v1 := strings.Split(version1,".")
	v2 := strings.Split(version2,".")
	
	for len(v1) < len(v2) {
		v1 = append(v1, "0")
	}
	for len(v2) < len(v1) {
		v2 = append(v2, "0")
	}

	l := len(v1)
	for i:=0; i<l; i++ {
		// 先把 00001 这种的左边的0全部清除
		vs1 := strings.TrimLeft(v1[i], "0")
		vs2 := strings.TrimLeft(v2[i], "0")
	
		// 补全长度，在右边加上"0"
		// 123 & 12345   =>   12300 & 12345
		for len(vs1) < len(vs2) {
			vs1 = "0" + vs1
		}
		for len(vs2) < len(vs1) {
			vs2 = "0" + vs2
		}

		vl := len(vs1)
		for j := 0; j < vl; j++ {
			if vs1[j] == vs2[j] {
				continue
			} else if (vs1[j] <vs2[j]) {
				return -1
			} else {
				return 1
			}
		}
	}
	return 0
}