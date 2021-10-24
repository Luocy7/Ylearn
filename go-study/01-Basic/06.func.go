package main

import (
	"fmt"
	"math"
	"reflect"
	"runtime"
)

func eval(a, b int, op string) (int, error) {
	switch op {
	case "+":
		return a + b, nil
	case "-":
		return a - b, nil
	case "*":
		return a * b, nil
	case "/":
		q, _, err := div(a, b)
		return q, err
	default:
		return 0, fmt.Errorf(
			"unsupported operation: %s", op)
	}
}

func add(a, b int) int {
	return a + b
}

// 函数可以有多个返回值，获取后不需要的可以填下划线_
func div(a, b int) (q, r int, err error) {
	if b == 0 {
		return q, r, fmt.Errorf("被除数为0")
	}
	q = a / b
	r = a % b
	return q, r, nil
}

// 函数式编程
func apply(op func(int, int) int, a, b int) int {
	p := reflect.ValueOf(op).Pointer()
	opName := runtime.FuncForPC(p).Name()
	fmt.Printf("Calling function %s with args "+
		"(%d, %d)\n", opName, a, b)

	return op(a, b)
}

// 可变参数列表
func sum(nums ...int) int {
	s := 0
	for i := range nums {
		s += nums[i]
	}
	return s
}

func main() {
	fmt.Println("Error handling")
	if result, err := eval(3, 4, "x"); err != nil {
		fmt.Println("Error:", err)
	} else {
		fmt.Println(result)
	}

	// 自动生成返回值快捷键Ctrl+Alt+V
	q, r, err := div(13, 0)
	fmt.Println(q, r, err)

	q, r, _ = div(13, 3)
	fmt.Printf("13 div 3 is %d mod %d\n", q, r)

	fmt.Println(apply(add, 1, 2))

	fmt.Println("pow(3, 4) is:", apply(
		func(a int, b int) int {
			return int(math.Pow(
				float64(a), float64(b)))
		}, 3, 4))

	fmt.Println("1+2+...+5 =", sum(1, 2, 3, 4, 5))
}
