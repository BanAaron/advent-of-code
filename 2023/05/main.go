package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
	"unicode"
)

func main() {
	file, err := os.Open("2023/05/data")
	if err != nil {
		panic(err)
	}

	defer func() {
		err := file.Close()
		if err != nil {
			panic(err)
		}
	}()

	var seeds []int

	scanner := bufio.NewScanner(file)
	var maps [][][3]int
	var currentMap [][3]int

	for scanner.Scan() {
		line := scanner.Text()
		if strings.Contains(line, "seeds") {
			split := strings.Split(line, " ")[1:]
			for _, s := range split {
				s, err := strconv.Atoi(s)
				if err != nil {
					panic(err)
				}
				seeds = append(seeds, s)
			}
		}

		if strings.Contains(line, "map") {
			maps = append(maps, currentMap)
		}

		var firstChar rune
		if len(line) > 0 {
			firstChar = rune(line[0])
		}
		if unicode.IsDigit(firstChar) {
			var store [3]int
			numbers := strings.Split(line, " ")
			for i, n := range numbers {
				n, err := strconv.Atoi(n)
				if err != nil {
					panic(err)
				}
				store[i] = n
			}
			currentMap = append(currentMap, store)
		}
	}
	maps = append(maps, currentMap)

	err = scanner.Err()
	if err != nil {
		panic(err)
	}

	maps = maps[1:]
	fmt.Println(maps)
}
