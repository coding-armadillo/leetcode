class Solution:
    def intToRoman(self, num: int) -> str:
        value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        ans = ""
        for i in range(len(value)):
            while num >= value[i]:
                num -= value[i]
                ans += roman[i]

        return ans
