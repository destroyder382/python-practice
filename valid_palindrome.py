# LeetCode 125. Valid Palindrome
# Проверить, является ли строка палиндромом, учитывая только буквы и цифры
# и игнорируя регистр.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = [char.lower() for char in s if char.isalnum()]
        s = ''.join(cleaned)
        return s == s[::-1]
