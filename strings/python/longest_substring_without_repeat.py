from typing import Optional


def longest_substring(s: Optional[str]) -> Optional[str]:
    """https://leetcode.com/problems/longest-substring-without-repeating-characters/"""
    if not s:
        return None
    visited = {}
    start = finish = max_length = tmp_start = 0
    for i in range(len(s)):
        if s[i] in visited and start <= visited[s[i]]:
            tmp_start = visited[s[i]] + 1
        else:
            tmp_length = i - tmp_start + 1
            if max_length < tmp_length:
                finish = i
                start = tmp_start
                max_length = tmp_length
        visited[s[i]] = i
    return s[start: finish + 1]  # len(s[start: finish + 1])


print(longest_substring('abcabcbb'))  # abc
print(longest_substring('bbbbb'))  # b
print(longest_substring('pwwkew'))  # wke
