package main

import (
	"fmt"
	"go-study/04-Interface/retriever/mock"
	"go-study/04-Interface/retriever/real"

	"time"
)

type Retriever interface {
	Get(url string) string
}

type Poster interface {
	Post(url string,
		form map[string]string) string
}

const url = "http://www.imooc.com"

func Download(r Retriever) string {
	return r.Get(url)
}

func Post(poster Poster) {
	poster.Post(url,
		map[string]string{
			"name":   "ccmouse",
			"course": "golang",
		})
}

// RetrieverPoster 组合接口
type RetrieverPoster interface {
	Retriever
	Poster
}

func session(s RetrieverPoster) string {
	s.Post(url, map[string]string{
		"contents": "another faked imooc.com",
	})
	return s.Get(url)
}

func inspect(r Retriever) {
	fmt.Println("Inspecting", r) // interface 肚子里是有东西的
	fmt.Printf(" > Type:%T Value:%v\n", r, r)

	// 如果需要区分多种类型，可以使用 switch 断言
	fmt.Print(" > Type switch: ")
	switch v := r.(type) {
	case *mock.Retriever:
		fmt.Println("Contents:", v.Contents)
	case *real.Retriever:
		fmt.Println("UserAgent:", v.UserAgent)
	}
	fmt.Println()
}

func main() {
	var r Retriever

	mockRetriever := mock.Retriever{
		Contents: "this is a fake imooc.com"}
	r = &mockRetriever
	inspect(r)

	r = &real.Retriever{
		UserAgent: "Mozilla/5.0",
		TimeOut:   time.Minute,
	}
	inspect(r)

	// 接口变量自带指针

	// Type assertion
	if mockRetriever, ok := r.(*mock.Retriever); ok {
		fmt.Println(mockRetriever.Contents)
		// ok==true 表明interface r 存储的是 *mock.Retriever 类型的值(这里赋值给了变量 mockRetriever)，反之则不是
	} else {
		fmt.Println("r is not a mock retriever")
	}

	fmt.Println(
		"Try a session with mockRetriever")
	fmt.Println(session(&mockRetriever))
}
