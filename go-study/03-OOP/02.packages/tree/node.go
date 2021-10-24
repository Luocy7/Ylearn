package tree

// Node 定义结构
type Node struct {
	Val         int
	Left, Right *Node
}

/*
	- 为结构定义的方法必须放在同一个包内
	- 可以使不同文件
*/
