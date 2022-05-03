from typing import Optional


def longest_substring(s: Optional[str]) -> Optional[str]:
    if not s:
        return None
    res = str()
    for i in range(len(s)):
        # non odd case: 'aba"
        tmp = helper(s, i, i)
        if len(tmp) > len(res):
            res = tmp
        # odd case: 'abba"
        tmp = helper(s, i, i + 1)
        if len(tmp) > len(res):
            res = tmp
    return res


def helper(s: str, left: int, right: int):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1: right]


print(longest_substring('babad'))  # bab
print(longest_substring('cbbd'))  # bb
print(longest_substring(None))  # None
print(longest_substring('a'))  # a
