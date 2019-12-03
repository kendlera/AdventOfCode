package main 

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func parseInput() []int {
	dat, err := ioutil.ReadFile("input.txt")
    if err != nil {
    	fmt.Println(err)
    	return nil
    }
    arr := strings.Split(string(dat), ",")
    var intified = []int{}
    for _, stringCodes := range arr {
        intCode, err := strconv.Atoi(stringCodes)
        if err != nil {
            panic(err)
        }
        intified = append(intified, intCode)
    }
    return intified
}


func main() {
	codes := parseInput()
	var currPos = 0
	var currValue = codes[0]
	var combinedVal = 0
	for currValue != 99 {
		if codes[currPos] == 1 {
			// addition!
			combinedVal = (codes[codes[currPos+1]] + codes[codes[currPos+2]])
		} else if codes[currPos] == 2 {
			combinedVal = (codes[codes[currPos+1]] * codes[codes[currPos+2]])
		} else {
			fmt.Println("Something went wrong!")
		}
		fmt.Printf("Pos %d: Opcode %d executes on (%d, %d) putting %d into pos %d\n", currPos, codes[currPos], 
			codes[codes[currPos+1]], codes[codes[currPos+2]], combinedVal, codes[currPos+3])
		codes[codes[currPos+3]] = combinedVal
		currPos += 4
		currValue = codes[currPos]
	}
	fmt.Printf("Final 0: %v\n", codes[0])
}