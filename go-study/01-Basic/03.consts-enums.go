package main

import "fmt"

func consts() {
	const (
		Van  = "scores.txt"
		a, b = 1, 2
	)
	var c int
	c = a + b
	fmt.Println(Van)
	fmt.Println(c)
}

func enums() {
	const (
		cpp = iota //表示自增
		java
		python
		golang
		javascript
		_
		mysql
	)

	const (
		b = 1 << (10 * iota) //自增表达式
		kb
		mb
		gb
		tb
		pb
	)
	fmt.Println(cpp, java, python, golang, javascript, mysql)
	fmt.Println(b, kb, mb, gb, tb, pb)
}

func main() {
	consts()
	enums()
}
