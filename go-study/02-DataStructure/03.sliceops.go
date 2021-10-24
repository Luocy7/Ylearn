package main

import "fmt"

func printSlice(s []int) {
	fmt.Printf("%v, len=%d, cap=%d\n",
		s, len(s), cap(s))
}

func sliceCreate() {
	fmt.Println("Creating slice")
	var s []int // Zero value for slice is nil

	for i := 0; i < 10; i++ {
		printSlice(s)
		s = append(s, 2*i+1)
	}
	fmt.Println(s)

	s1 := []int{2, 4, 6, 8}
	printSlice(s1)

	s2 := make([]int, 16)
	s3 := make([]int, 10, 32)
	printSlice(s2)
	printSlice(s3)
}

func sliceAppend() {
	arr := [...]int{0, 1, 2, 3, 4, 5, 6, 7}
	fmt.Printf("arr = %v\n", arr)
	s1 := arr[2:6]
	printSlice(s1)
	s2 := s1[3:5]
	printSlice(s2)
	s3 := append(s2, 10) // append改动切片会影响到底层数组
	printSlice(s3)
	s4 := append(s3, 11) // 这时底层的数组重新分配变化了
	printSlice(s4)
	s5 := append(s4, 12)
	printSlice(s5)
	fmt.Printf("arr = %v\n", arr)
}

func sliceCopy() {
	s1 := []int{2, 4, 6, 8}
	s2 := make([]int, len(s1)) // 需要预先分配空间
	fmt.Println("Copying slice")
	copy(s2, s1)
	printSlice(s2)
}

func sliceDelete() {
	s1 := []int{2, 4, 6, 8, 10}
	printSlice(s1)
	fmt.Println("Deleting second element from slice")
	s1 = append(s1[:1], s1[2:]...) // 删除s1[1] 即在s1[:1]之后添加s1[2:] 以及可变元素...
	printSlice(s1)

	fmt.Println("Popping from front")
	front := s1[0]
	s1 = s1[1:]

	fmt.Println(front)
	printSlice(s1)

	fmt.Println("Popping from back")
	tail := s1[len(s1)-1]
	s1 = s1[:len(s1)-1]

	fmt.Println(tail)
	printSlice(s1)
}

func main() {
	sliceCreate()
	sliceAppend()
	sliceCopy()
	sliceDelete()
}
