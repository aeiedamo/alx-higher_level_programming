#!/usr/bin/python3
def roman_to_int(roman_string):
    num = 0
    if roman_string and type(roman_string) == str:
        romanDigits = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                       'C': 100, 'D': 500, 'M': 1000}
        for romanNum in reversed(roman_string):
            HinduArabic = romanDigits[romanNum]
            if num < (HinduArabic * 5):
                num += HinduArabic
            else:
                num -= HinduArabic
    return (num)
