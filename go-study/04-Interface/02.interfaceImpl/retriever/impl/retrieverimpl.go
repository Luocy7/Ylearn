package impl

import (
	"net/http"
	"net/http/httputil"
)

type RetrieverImpl struct {
}

// Get 只要实现了接口里的方法就认为实现了方法，无须耦合地指定Retriever接口
func (r RetrieverImpl) Get(url string) string {
	resp, err := http.Get(url)
	if err != nil {
		panic(err)
	}
	result, err := httputil.DumpResponse(resp, true)
	closeErr := resp.Body.Close()
	if closeErr != nil {
		return ""
	}
	if err != nil {
		panic(err)
	}
	return string(result)
}
