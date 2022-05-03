package main

import (
	"fmt"
	"strings"
)

func longestSubstringWithoutRepeat(s string) (res string) {
	// https://leetcode.com/problems/longest-substring-without-repeating-characters/
	if s == "" {
		return res
	}
	sSlice := strings.Split(s, "")
	start, finish, maxLength, tmpStart := 0, 0, 0, 0
	visited := make(map[string]int)
	for i := range s {
		if val, ok := visited[sSlice[i]]; ok && start <= val {
			tmpStart = visited[sSlice[i]] + 1
		} else {
			tmpLength := i - tmpStart + 1
			if maxLength < tmpLength {
				finish = i
				start = tmpStart
				maxLength = tmpLength
			}
		}
		visited[sSlice[i]] = i
	}
	return s[start : finish+1]
}

func main() {
	fmt.Println(longestSubstringWithoutRepeat("abcabcbb")) // abc
	fmt.Println(longestSubstringWithoutRepeat("bbbbb"))    // b
	fmt.Println(longestSubstringWithoutRepeat("pwwkew"))   // "wke"
}
