from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lengths = [len(s) for s in strs]
        if 0 in lengths or not lengths:
            return ""
        else:
            result = ""
            index = 0

            while index < min(lengths):
                character = set([s[index] for s in strs])
                if len(character) > 1:
                    break
                else:
                    result += character.pop()
                    index += 1

            return result
