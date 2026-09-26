# LeetCode 217. Contains Duplicate
# Дан массив nums, вернуть True, если есть хотя бы одно повторяющееся значение.

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums2 = set(nums)
        return len(nums) != len(nums2)
