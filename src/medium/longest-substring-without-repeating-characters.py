class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        substr = ""
        rear = 0

        for front in range(len(s)):
            if s[front] not in substr:
                substr += s[front]
            else:
                max_len = max(max_len, len(substr))
                while s[rear] != s[front]:
                    rear += 1
                rear += 1
                substr = s[rear : front + 1]

        return max(max_len, len(substr))
