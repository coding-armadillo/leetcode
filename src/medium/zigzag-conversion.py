class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = []
        a = 2 * numRows - 2
        for i in range(a):
            rows.append([])

        for i in range(len(s)):
            ind = i % a
            if ind >= numRows:
                ind = a - ind
            rows[ind].append(s[i])

        result = ""
        for i in range(a):
            result += "".join(rows[i])

        return result
