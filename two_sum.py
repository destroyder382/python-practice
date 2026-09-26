# LeetCode 1. Two Sum
# Дан массив nums и число target, найти индексы двух чисел, чья сумма равна target.

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        res = {}
        for index, num in enumerate(nums):
            needed = target - num
            if needed in res:
                return [res[needed], index]
            else:
                res[num] = index
        return []
