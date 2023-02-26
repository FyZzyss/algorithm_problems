def roman_to_int(s: str) -> int:
    value_mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = prev_value = 0
    for i in range(len(s) - 1, -1, -1):
        if value_mapping[s[i]] >= prev_value:
            result += value_mapping[s[i]]
        else:
            result -= value_mapping[s[i]]
        prev_value = value_mapping[s[i]]
    return result

print(roman_to_int("III"))    # 3
print(roman_to_int("LVIII"))  # 58
print(roman_to_int("MCMXCIV"))  # 1994
