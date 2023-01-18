class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        size = len(s)
        prev = None
        ans = 0
        s = s[::-1]
        for i in range(size):
            if prev and roman[s[i]] < prev:
                ans -= 2 * roman[s[i]]
            ans += roman[s[i]]
            prev = roman[s[i]]
        return ans
