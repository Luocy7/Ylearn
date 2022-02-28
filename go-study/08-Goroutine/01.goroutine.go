package main

import (
	"fmt"
	"time"
)

// goroutine定义：函数加上go可给调度器运行、无需区分异步函数、调度器在合适时切换
// goroutine可能切换的点：I/O，select，channel，等待锁，函数调用(有时)，runtime.Gosched()

func main() {
	var a [10]int
	// 10个协程映射到实际的核数个线程内执行
	for i := 0; i < 10; i++ {
		// 使用协程并发执行函数(匿名)，并传参保证内部的i隔离
		go func(i int) {
			for {
				//fmt.Printf("Hello from goroutine %d\n", i)
				a[i]++
				// 手动交出控制权，防止无限占用，使别的协程有机会运行(较公平)，一般也可不用
				// 协程是非抢占式的 不是操作系统层面的多任务（线程）
				//runtime.Gosched()
			}
		}(i) // 此处需要传参保证内部的i隔离（闭包）可用go run -race goroutine.go 检测数据冲突
	}
	// 延迟main退出时间，使打印来得及
	time.Sleep(time.Millisecond)
	// 打印结果
	fmt.Println(a)
}
