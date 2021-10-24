package main

import "fmt"

func lengthOfNonRepeatingSubStr(s string) int {
	lastOccurred := make(map[rune]int)
	start := 0
	maxLen := 0
	for i, ch := range []rune(s) {
		// 该字符ch出现过而且在start后（遇到重复字符）时，需要把start移到该ch后一位使得ch不重复（消除重复）
		if lastI, exist := lastOccurred[ch]; exist && lastI >= start {
			start = lastI + 1
		}
		// 记录最大长度
		if i-start+1 > maxLen {
			maxLen = i - start + 1
		}
		// 记录该字符位置
		lastOccurred[ch] = i
	}
	return maxLen
}

func main() {
	fmt.Println(
		lengthOfNonRepeatingSubStr("abcabcbb"))
	fmt.Println(
		lengthOfNonRepeatingSubStr("bbbbb"))
	fmt.Println(
		lengthOfNonRepeatingSubStr("pwwkew"))
	fmt.Println(
		lengthOfNonRepeatingSubStr(""))
	fmt.Println(
		lengthOfNonRepeatingSubStr("b"))
	fmt.Println(
		lengthOfNonRepeatingSubStr("abcdef"))
	fmt.Println(
		lengthOfNonRepeatingSubStr("天青色等烟雨而我在等你"))
	fmt.Println(
		lengthOfNonRepeatingSubStr("一二三二一"))
	fmt.Println(
		lengthOfNonRepeatingSubStr(
			"黑化肥挥发发灰会花飞灰化肥挥发发黑会飞花"))
}
