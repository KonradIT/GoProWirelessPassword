package main

import (
	 "math/rand"
	 "fmt"
	 "strconv" 
	 "time"
	 "io/ioutil"
	 "strings"
	 "bufio"
	 "os"
)
func gen_part1() string{
	dictionary1 := []string{"sports","hike","vault","skate","share","sail","sled","wave","dive","scuba","dude","sport","canoe","tennis","action"}
	sportsfile, _ := ioutil.ReadFile("sportslist.txt")
	dictionary2 := strings.Split(string(sportsfile), ",")
	dictionary_final := append(dictionary1, dictionary2...)
	dic_len := len(dictionary_final)
	return dictionary_final[rand.Intn(dic_len)]
}

func gen_part2() string{
	sequence := ""
	for i := 0; i < 4; i++ {
			sequence += strconv.Itoa(rand.Intn(9)) // 0 - 9
	}
	return sequence
}

func main(){
    rand.Seed(time.Now().UnixNano())
	//fmt.Printf("%s%s", gen_part1(),gen_part2())
	reader := bufio.NewReader(os.Stdin)
    fmt.Print("Enter password: ")
    passwd, _ := reader.ReadString('\n')
    passwd = passwd[:len(passwd)-1]
    fmt.Println(passwd)
    found := false
    for found == false {
    	guess := gen_part1() + gen_part2()
    	fmt.Println(guess)
    	if guess == passwd{
    		found = true
    		fmt.Println(guess)
    	}
    }
	
}
