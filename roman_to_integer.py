# LeetCode 13. Roman to Integer
# Перевести римское число (строку) в обычное целое число.

class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        for i in range(len(s)):
            if i < len(s) - 1 and values[s[i]] < values[s[i + 1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]
        return total
