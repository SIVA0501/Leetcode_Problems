class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        res = []
        for i in range(len(nums)):
            if nums[i] != 0:
                res.append(nums[i])
        zero_count = nums.count(0)
        for i in range(zero_count):
            res.append(0)
        for i in range(len(nums)):
            nums[i] = res[i]
        