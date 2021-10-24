package main

import (
	"fmt"
)

func tryDefer() {
	// defer能保证在return或panic使函数返回前能执行，顺序是先进后出(栈)，一般用于成对对应的操作
	defer fmt.Println(1)
	defer fmt.Println(2)
	fmt.Println(3)
	// 模拟函数执行中断
	panic("break")
	fmt.Println(4)
}

func main() {
	tryDefer()
}
