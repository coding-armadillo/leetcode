from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        phone_dict = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        def dfs(num, string, result):
            if num == length:
                result.append(string)
                return
            for letter in phone_dict[digits[num]]:
                dfs(num + 1, string + letter, result)

        result = []

        length = len(digits)
        dfs(0, "", result)

        return result
