from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        size = len(height)
        l = 0
        r = size - 1
        maxWater = 0
        while l < r:
            water = (r - l) * min(height[l], height[r])
            if water > maxWater:
                maxWater = water

            if height[l] < height[r]:
                l = l + 1
            else:
                r = r - 1

        return maxWater
