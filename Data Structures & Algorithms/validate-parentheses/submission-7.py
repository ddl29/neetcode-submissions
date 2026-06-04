class Solution:
    def isValid(self, s: str) -> bool:
        opening = {"(", "[", "{"}
        map = {")": "(", "]": "[", "}": "{"}
        stack = []
        for c in s:
            if c in opening:
                stack.append(c)
            else:
                if len(stack) == 0 or stack.pop() != map[c]:
                    return False
        if len(stack) > 0:
            return False
        return True