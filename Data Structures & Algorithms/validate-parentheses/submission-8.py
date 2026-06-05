class Solution:
    def isValid(self, s: str) -> bool:
        opening = {"{", "[", "("}
        myDict = {")": "(", "]":"[", "}":"{"}
        stack = []
        for c in s:
            if c in opening:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                else:
                    if stack.pop() != myDict[c]:
                        return False
        if len(stack) != 0:
            return False
        return True