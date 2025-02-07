class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        s = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in s:
                return[s[diff], i]
            s[num] = i

        return []