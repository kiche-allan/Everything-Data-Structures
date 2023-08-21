# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        
        total = 0
        prev_value = 0
        
        for letter in roman[::-1]:
            value = roman_map[letter]
            if value >= prev_value:
                total += value
            else:
                total -= value
            prev_value = value
        return total