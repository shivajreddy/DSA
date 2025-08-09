package main

import (
	"fmt"
	"bufio"
	"os"
)

func readFile() {
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("ERROR OPENING FILE")
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		fmt.Println(line)
	}

	if err := scanner.Err(); err != nil {
		fmt.Println("Error wihle reading file", err)
	}
}

func main() {
	readFile()
}
