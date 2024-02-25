from typing import Optional


def longest_substring(s: Optional[str]) -> Optional[str]:
    """https://leetcode.com/problems/longest-palindromic-substring/"""
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


def longest_substring_manacher(s: str) -> str:
    if len(s) <= 1:
        return s
    start = 0
    max_str = s[0]
    max_len = 1
    s = f'#{"#".join(s)}#'
    dp = [0] * len(s)
    center = radius = 0
    for i in range(len(s)):
        if i < radius:
            dp[i] = min(radius - i, dp[2 * center - i])
        while i - dp[i] - 1 >= 0 and i + dp[i] + 1 < len(s) and s[i - dp[i] - 1] == s[i + dp[i] + 1]:
            dp[i] += 1
        if i + dp[i] > radius:
            center = i
            radius = i + dp[i]
        if dp[i] > max_len:
            max_len = dp[i]
            start = i
    max_str = s[start - dp[start]: start + dp[start] + 1].replace('#', '') if max_len > 1 else max_str
    return max_str


print(longest_substring('babad'))  # bab
print(longest_substring('cbbd'))  # bb
print(longest_substring(None))  # None
print(longest_substring('a'))  # a
