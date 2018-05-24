/*
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.
翻译：有一个数组，其中存放的都是数字，给这个数组加1，求结果。这相当于把一个数的每一位都看做是数组的一个元素，给这个数加1，
得到新的数。我们从后往前进行遍历，如果有进位一次向前一位加1,直到没有进位的时候返回数组即可。但是，
要注意如果数组中所有的元素都是9的话，这是最坏的情况，每一步都需要进位，这时候定义一个新的数组用来存放结果。

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
*/

package main

import (
	"fmt"
)

/*func plusOne(digits []int) []int {
	str := ""
	for _,v:=range digits{
		str+=strconv.Itoa(v)
	}
	i,_:=strconv.Atoi(str)
	i++//长度只有int
	fmt.Println(i)//int 10
	str = strconv.Itoa(i)
	//newArray := [len(str)]int{}//go 无法使用非常量定义新数组
	newArray := make([]int, len(str))
	for a := range str{//10
		b := math.Pow10(len(str)-1)
		newArray[a] = i / int(b)
		i = i % int(b)
		str = str[1:]
		//fmt.Println(str,i, digits[a], b)
		if(str == ""){
			break
		}
		//fmt.Println(newArray)
		//digits = newArray
	}
	return newArray
}*/

//4ms
func plusOne(digits []int) []int {
	var n int = len(digits)
	for i:= n-1; i>=0; i--{
		if digits[i] < 9 {
			digits[i]+=1
			return digits
		} else {
			digits[i] = 0
		}
	}
	var a = make([]int,n+1)
	a[0] = 1
	return a

}

func main() {
	//a := []int{1,2,3}
	//a := []int{4,3,2,1}
	a := []int{9}
	a = []int{7,2,8,5,0,9,1,2,9,5,3,6,6,7,3,2,8,4,3}
	fmt.Println(plusOne(a))
}
