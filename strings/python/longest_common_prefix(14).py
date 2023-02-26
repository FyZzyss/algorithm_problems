from typing import List


def longest_common_prefix(strs: List[str]) -> str:
    max_prefix = min(strs, key=lambda x: len(x))
    while max_prefix:
        if all(word[:len(max_prefix)] == max_prefix for word in strs):
            return max_prefix
        max_prefix = max_prefix[:-1]
    return max_prefix
