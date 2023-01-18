class Solution:
    def reverse(self, x: int) -> int:
        digits = str(x)[::-1]
        ans = int(digits) if x >= 0 else int(digits[:-1])
        if ans > 2**31:
            ans = 0

        return ans if x > -0 else -ans
