class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ["(", "[", "{"]:
                stack.append(char)
            elif char in [")", "]", "}"]:
                if len(stack) == 0:
                    return False
                last = stack.pop()
                if char == ")" and last != "(":
                    return False
                elif char == "]" and last != "[":
                    return False
                elif char == "}" and last != "{":
                    return False

        return len(stack) == 0
        