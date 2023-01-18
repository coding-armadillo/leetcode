from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        t = {}
        l = len(nums)

        for i in range(l):
            if nums[i] not in t:
                t[nums[i]] = [i]
            else:
                t[nums[i]].append(i)

        for i in range(l):
            lookup = target - nums[i]
            if lookup != nums[i]:
                if lookup in t:
                    return (i, t[lookup][0])
            else:
                if len(t[lookup]) > 1:
                    return (t[lookup][0], t[lookup][1])
