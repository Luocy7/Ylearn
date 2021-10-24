package main

import (
	"bufio"
	"errors"
	"fmt"
	"os"
)

func writeFile(filename string) {
	// 建立文件create对应关闭操作close
	file, err := os.Create(filename)
	if err != nil {
		// 处理错误
		fmt.Println("处理文件出错 ->", err)
		// 进入源码可以看该err可以转换成什么类型
		// If there is an error, it will be of type *PathError.
		pathError := err.(*os.PathError)
		fmt.Printf("pathError.Op = %s\npathError.Path = %s\npathError.Err = %s\n",
			pathError.Op,
			pathError.Path,
			pathError.Err,
		)
		return
	}
	defer func(file *os.File) {
		err := file.Close()
		if err != nil {

		}
	}(file)

	// 建立writer对应flush
	writer := bufio.NewWriter(file)
	defer func(writer *bufio.Writer) {
		err := writer.Flush()
		if err != nil {

		}
	}(writer)

	for i := 1; i <= 10; i++ {
		_, err := fmt.Fprintf(writer, "%d\n", i)
		if err != nil {
			panic(err)
		}
	}
}

func main() {
	// 测试错误处理
	writeFile("hello.txt")

	// 可建立自己的error
	err := errors.New("my error")
	fmt.Println(err)
}
