class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = defaultdict(list)
        for s in strs:
            alphabet = [0]*26
            for c in s:
                alphabet[ord(c) - 97] += 1

            myDict[tuple(alphabet)].append(s)
        return list(myDict.values())