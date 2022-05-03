package main

import "fmt"

func longestSubstring(s string) (res string) {
    // https://leetcode.com/problems/longest-palindromic-substring/
	if s == "" {
		return res
	}
	for i := range s {
		tmp := helper(s, i, i)
		if len(tmp) > len(res) {
			res = tmp
		}
		tmp = helper(s, i, i+1)
		if len(tmp) > len(res) {
			res = tmp
		}
	}
	return res
}

func helper(s string, left, right int) (res string) {
	for left >= 0 && right < len(s) && s[left] == s[right] {
		left = left - 1
		right = right + 1
	}
	return s[left+1 : right]
}

func main() {
	fmt.Println(longestSubstring("babad")) // bab
	fmt.Println(longestSubstring("cbbd"))  // bb
	fmt.Println(longestSubstring(""))      // ""
	fmt.Println(longestSubstring("a"))     // a
}
