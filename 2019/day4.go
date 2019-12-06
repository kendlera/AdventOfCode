package main 

import (
	"fmt"
	"strconv"
)

func isSorted(value int) bool {
	// assumes a 6 digit value
	hundredThousands := int(value / 100000)
	discard := hundredThousands * 100000
	tenThousands := int((value-discard) / 10000)
	discard += (tenThousands * 10000)
	thousands := int((value-discard) / 1000)
	discard += (thousands * 1000)
	hundreds := int((value-discard) / 100)
	discard += (hundreds * 100)
	tens := int((value-discard) / 10)
	discard += (tens * 10)
	ones := value-discard
	return ((hundredThousands <= tenThousands) && (tenThousands <= thousands) && (thousands <= hundreds) && (hundreds <= tens) && (tens <= ones))
}

// check that an adjacent pair matches, but not with anything to either side
func hasDouble(value int) bool {
	strValue := strconv.Itoa(value)
	return (((strValue[0] == strValue[1]) && (strValue[1] != strValue[2])) || 
		((strValue[1] == strValue[2]) && (strValue[0] != strValue[1]) && (strValue[2] != strValue[3])) || 
		((strValue[2] == strValue[3]) && (strValue[1] != strValue[2]) && (strValue[3] != strValue[4])) || 
		((strValue[3] == strValue[4]) && (strValue[2] != strValue[3]) && (strValue[4] != strValue[5])) || 
		((strValue[4] == strValue[5]) && (strValue[3] != strValue[4])))
}

func main() {
	adjustedMin := 246666
	adjustedMax := 779999
	numPasswords := 0
	for adjustedMin <= adjustedMax {
		if (isSorted(adjustedMin) && hasDouble(adjustedMin)) {
			numPasswords += 1
		}
		adjustedMin += 1
	}
	fmt.Printf("Total Passwords: %d", numPasswords)
}