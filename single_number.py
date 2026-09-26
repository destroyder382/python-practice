# LeetCode 136. Single Number
# В массиве каждое число встречается дважды, кроме одного. Найти это число.

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result
