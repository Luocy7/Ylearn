package main

import (
	"fmt"
	"go-study/03-oop/03.extend/queue"
)

func main() {
	q := queue.MyQueue{1}
	fmt.Println(q)
	q.Push(2)
	q.Push(3)
	fmt.Println(q)
	fmt.Println(q.Pop())
	fmt.Println(q.Pop())
	fmt.Println(q.IsEmpty())
	fmt.Println(q.Pop())
	fmt.Println(q.IsEmpty())
}
