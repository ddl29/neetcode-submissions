class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # option 0: check len

        # option 1: frequency map

        # option 2: sort & compare if equal

        if len(s) != len(t): return False

        def sortStr(string):
            return "".join(sorted(string))

        return sortStr(s) == sortStr(t)