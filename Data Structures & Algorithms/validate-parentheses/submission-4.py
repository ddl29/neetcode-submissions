class Solution:
    def isValid(self, s: str) -> bool:
        opening = set(['(', '[', '{'])
        stack = []
        for c in s:
            if c in opening:
                stack.append(c);
            else:
                if (len(stack) == 0): return False
                expectedOpening = stack.pop();
                invalid = (c == ')' and expectedOpening != '(') or (c == ']' and expectedOpening != '[') or (c == '}' and expectedOpening != '{')
                if invalid:
                    return False
        if len(stack) > 0: return False
        return True