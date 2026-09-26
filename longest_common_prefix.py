# LeetCode 14. Longest Common Prefix
# Найти самый длинный общий префикс среди всех строк массива.

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = strs[0]
        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
        return prefix
