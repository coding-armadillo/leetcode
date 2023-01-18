from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        ans = 0
        mid = nums[len(nums) // 2]
        min_diff = abs(nums[0] + mid + nums[len(nums) - 1] - target)

        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                value = nums[i] + nums[l] + nums[r]
                if value == target:
                    return target
                diff = abs(value - target)
                if diff <= min_diff:
                    min_diff = diff
                    ans = value
                if value > target:
                    r -= 1
                if value < target:
                    l += 1

        return ans
