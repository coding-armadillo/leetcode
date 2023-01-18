class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        a = 1
        while x // a:
            a *= 10
        a //= 10

        while x:
            r = x % 10
            l = x // a
            if l != r:
                return False
            x = (x - l * a) // 10
            a = a // 100

        return True
