from typing import Dict, List

# PROBLEM STATEMENT
# https://leetcode.com/problems/integer-to-roman/description/
#
# Roman numerals are formed by appending the conversions of decimal place values
# from highest to lowest. Converting a decimal place value into a Roman numeral
# has the following rules:
#
# - If the value does not start with 4 or 9, select the symbol of the maximal
#   value that can be subtracted from the input, append that symbol to the result,
#   subtract its value, and convert the remainder to a Roman numeral.
#
# - If the value starts with 4 or 9 use the subtractive form representing one
#   symbol subtracted from the following symbol, for example, 4 is 1 (I) less
#   than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following
#   subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
#
# - Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times
#   to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D)
#   multiple times. If you need to append a symbol 4 times use the subtractive form.
#
# Given an integer, convert it to a Roman numeral.
#
# CONSTRAINTS
# 1 <= num <= 3999
#
# EXAMPLES
# Input     num = 3749
# Output    "MMMDCCXLIX"
#
# Input     num = 58
# Output    "LVIII"
#
# Input     num = 1994
# Output    "MCMXCIV"

roman_map: Dict[int, str] = {
    1000: "M",
     900: "CM",
     500: "D",
     400: "CD",
     100: "C",
      90: "XC",
      50: "L",
      40: "XL",
      10: "X",
       9: "IX",
       5: "V",
       4: "IV",
       1: "I"
}

def intToRoman(num: int) -> str:
    # NOTE: A purely arithmetic approach becomes unwieldy.
    # Roman numerals are more naturally expressed as a rule-based system
    # with explicit additive and subtractive symbols.
    result: List[str] = []

    for key, value in roman_map.items():
        if num == 0: break

        n = num // key

        if (n > 0):
            result.append(value * n)
            num %= key

    return "".join(result)

if __name__ == '__main__':
    # examples
    assert intToRoman(3749) == "MMMDCCXLIX"
    assert intToRoman(58) == "LVIII"
    assert intToRoman(1994) == "MCMXCIV"
