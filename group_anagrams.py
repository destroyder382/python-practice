# LeetCode 49. Group Anagrams
# Дан массив строк, сгруппировать анаграммы вместе.

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]
        return list(groups.values())
