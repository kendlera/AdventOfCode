package main 

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
	"os"
)

func parseInput() []string {
	path, _ := os.Getwd()
	fmt.Println(path)
	dat, err := ioutil.ReadFile("input.txt")
    if err != nil {
    	fmt.Println("Failed to Read file")
    	fmt.Println(err)
    	return nil
    }
    arr := strings.Split(string(dat), "\r\n")
    return arr
}

func calculateFuel(item int) int {
	var total = 0
	for item > 6 { // weight 6 gives us free fuel
		fuel := (int(item / 3) - 2)
		total += fuel 
		item = fuel 
	}
	return total 
}

func main() {
	var total = 0
	modules := parseInput()
	for _, module := range modules {
		fmt.Printf("Current Total: %d, Evaluating: %s\n", total, module)
		moduleInt, err := strconv.Atoi(module) 
		if (err != nil) {
			fmt.Println(err)
		}
		fuel := calculateFuel(moduleInt)
		fmt.Printf("Fuel: %d\n", fuel)
		total += fuel 
	}
	fmt.Printf("Total Fuel: %v\n", total)
}
// 17446 too low