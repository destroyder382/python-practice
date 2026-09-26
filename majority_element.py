# LeetCode 169. Majority Element
# Найти элемент, который встречается в массиве больше n/2 раз.

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums1 = sorted(nums)
        index = len(nums) // 2
        return nums1[index]
