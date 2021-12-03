package main

import (
	"fmt"
	"go-study/04-Interface/02.interfaceImpl/retriever"
	"go-study/04-Interface/02.interfaceImpl/retriever/impl"
)

func getBaiduIndex(r retriever.Retriever) string {
	return r.Get("http://www.baidu.com")
}

func main() {
	var r retriever.Retriever
	r = impl.RetrieverImpl{}
	fmt.Println(getBaiduIndex(r))
}
