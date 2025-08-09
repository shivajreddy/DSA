package main

import (
	"fmt"
	"strconv"
	"os"
	"bufio"
)

func solution(s string) string {
	n := len(s)
	if n > 10 {
		first_char := string(s[0])
		last_char := string(s[n-1])
		return first_char + strconv.Itoa(n-2) + last_char
	}
	return s
}

func main(){

	sc := bufio.NewScanner(os.Stdin)
	sc.Scan()

	t, _ := strconv.Atoi(sc.Text())
	for i := 0; i < t; i++ {
		sc.Scan()
		word := sc.Text()
		fmt.Println(solution(word))
	}

}

