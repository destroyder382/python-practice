# LeetCode 283. Move Zeroes
# Дан массив nums, переместить все нули в конец, сохранив порядок остальных
# элементов, без создания нового массива (in-place).

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        insert_pos = 0
        for index, value in enumerate(nums):
            if value != 0:
                nums[insert_pos] = nums[index]
                insert_pos += 1
        for i in range(insert_pos, len(nums)):
            nums[i] = 0
