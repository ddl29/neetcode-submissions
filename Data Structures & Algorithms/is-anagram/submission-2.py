class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        # frequency map
        myDict = {}
        for c in s:
            if c in myDict:
                myDict[c]+=1
            else:
                myDict[c] = 1
        
        for c in t:
            if c in myDict:
                if myDict[c] == 0:
                    return False
                myDict[c]-=1
            else:
                return False
        return True