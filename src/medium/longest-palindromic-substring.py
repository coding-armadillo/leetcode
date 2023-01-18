class Solution:
    def findPalindrome(self, s: str, l: int, r: int) -> str:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1 : r]

    def longestPalindrome(self, s: str) -> str:
        result = ""
        for i in range(len(s)):
            # ABA
            type1 = self.findPalindrome(s, i, i)
            if len(type1) > len(result):
                result = type1
            # ABBA
            type2 = self.findPalindrome(s, i, i + 1)
            if len(type2) > len(result):
                result = type2

        return result
