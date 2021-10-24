package main

import (
	"fmt"
	"strings"
	"unicode/utf8"
)

func main() {
	s := "Today天青色等烟雨 而我在等你~"
	fmt.Println(s)
	fmt.Println("len(s) =", len(s))

	// 打印byte[]
	for _, b := range []byte(s) {
		fmt.Printf("%X ", b)
	}
	fmt.Println()

	// 打印rune十六进制(int32)  Unicode编码
	for i, ch := range s { // ch is a rune
		fmt.Printf("(%d %X)", i, ch)
	}
	fmt.Println()

	//  使用utf8库打印相关数字
	fmt.Println("Rune Count In String(s) =",
		utf8.RuneCountInString(s))

	//  使用utf8库解码byte成一个个的rune
	bytes := []byte(s)
	for len(bytes) > 0 {
		ch, size := utf8.DecodeRune(bytes)
		bytes = bytes[size:]
		fmt.Printf("%c %d %X\n", ch, ch, ch)
	}
	fmt.Println()

	// 直接打印rune
	for i, ch := range []rune(s) {
		fmt.Printf("(%d %c) ", i, ch)
	}
	fmt.Println()

	// 修改rune测试
	s2 := []rune(s)
	s2[2] = '上'
	fmt.Println(string(s2))
	fmt.Println(s)

	// 字符串其它操作
	fmt.Println(strings.Split(s, " "))
	fmt.Println(strings.Contains(s, "烟雨"))
	fmt.Println(strings.Replace(s, "Today", "Tomorrow", -1))
}
