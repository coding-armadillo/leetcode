from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        for i in range(len(nums) - 2):
            if i == 0 or nums[i] > nums[i - 1]:
                l = i + 1
                r = len(nums) - 1
                while l < r:
                    if nums[i] + nums[l] + nums[r] == 0:
                        ans.append([nums[i], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    elif nums[i] + nums[l] + nums[r] > 0:
                        while l < r:
                            r -= 1
                            if nums[r] < nums[r + 1]:
                                break
                    else:
                        while l < r:
                            l += 1
                            if nums[l] > nums[l - 1]:
                                break

        return ans
