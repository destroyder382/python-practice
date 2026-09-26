# LeetCode 242. Valid Anagram
# Проверить, являются ли строки s и t анаграммами друг друга.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
