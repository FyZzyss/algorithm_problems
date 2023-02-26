def is_palindrome_str(x: int) -> bool:
    new_x = str(x)
    left = 0
    right = len(new_x) - 1
    while left < right:
        if new_x[left] != new_x[right]:
            return False
        left += 1
        right -= 1
    return True

def is_palindrome_int(x: int) -> bool:
    if x < 0:
        return False
    new_x = x
    palindrome = 0
    while new_x > 0:
        palindrome = palindrome * 10 + new_x % 10
        new_x = new_x // 10

    return x == palindrome


def is_palindrome_half_int(x: int) -> bool:
    if x < 0 or (x > 0 and x % 10 == 0):
        return False
    palindrome = 0
    while x > palindrome:
        palindrome = palindrome * 10 + x % 10
        x = x // 10

    return x == palindrome or x == palindrome // 10


print(is_palindrome_half_int(-121))  # False
print(is_palindrome_half_int(121))   # True
print(is_palindrome_half_int(1221))  # True
print(is_palindrome_half_int(0))     # True
print(is_palindrome_half_int(10))    # False
