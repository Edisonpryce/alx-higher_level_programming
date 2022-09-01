#!/usr/bin/python3
def roman_to_int(roman_string):
    total = 0

    roman_numbers = {
                    "I": 1, "V": 5, "X": 10, "L": 50,
                    "C": 100, "D": 500, "M": 1000
                    }

    if not isinstance(roman_string, str) or not roman_string:
        return 0

    numbers = [roman_numbers[i] for i in roman_string]

    for i in range(len(numbers) - 1):
        if numbers[i + 1] > numbers[i]:
            numbers[i + 1] -= numbers[i]
        else:
            total += numbers[i]
    total += numbers[len(numbers) - 1]

    return total
