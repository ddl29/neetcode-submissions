class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = defaultdict(list)
        for s in strs:
            myDict["".join(sorted(s))].append(s)
        #here we have a dictionary of lists, grouped anagrams
        return list(myDict.values())