package mock

import "fmt"

type Retriever struct {
	Contents string
}

// go没有显示的implement来实现接口，默认实现接口的所有方法即为实现接口
// 通过这种形式来实现duck typing

func (r *Retriever) Get(url string) string {
	return r.Contents
}

func (r *Retriever) Post(url string,
	form map[string]string) string {
	r.Contents = form["contents"]
	return "ok"
}

// 系统接口stringer 类似于toString
func (r *Retriever) String() string {
	return fmt.Sprintf(
		"Retriever: {Contents=%s}", r.Contents)
}
