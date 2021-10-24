package main

import (
	"bufio"
	"fmt"
	"io"
	"strings"
)

// 函数是一等公民：参数、变量、返回值都可以是函数

// 闭包 > 函数体 = 局部变量 + 自由变量
func adder() func(int) int {
	sum := 0
	return func(v int) int {
		sum += v
		return sum
	}
}

// 给函数定义别名，便于实现接口(方法)
type intGenerator func() int

// 函数别名扩展实现Reader接口(方法)
func (ig intGenerator) Read(p []byte) (n int, err error) {
	// 由于不断提供扫描输出，因此需要设立循环终止条件
	next := ig()
	if next > 10000 {
		return 0, io.EOF
	}
	// 格式化输出返回值next
	s := fmt.Sprintf("%d\n", next)
	// 使用代理实现方法，当p[]太小时会读不完
	return strings.NewReader(s).Read(p)
}

func fib() func() int {
	a, b := 0, 1
	return func() int {
		a, b = b, a+b
		return a
	}
}

// 函数定义
func fibo() intGenerator {
	a, b := 0, 1
	return func() int {
		a, b = b, a+b
		return a
	}
}

// 如果能读就不断扫描输出
func printReaderContents(reader io.Reader) {
	scanner := bufio.NewScanner(reader)
	for scanner.Scan() {
		fmt.Println(scanner.Text())
	}
}

func main() {
	fmt.Println("adder:")
	a := adder()
	for i := 0; i < 10; i++ {
		fmt.Println(a(i))
	}
	fmt.Println()

	fmt.Println("fib:")
	ig := fibo()
	printReaderContents(ig)
}
