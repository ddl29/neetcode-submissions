class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict = {}
        for num in nums:
            if num in myDict:
                myDict[num] += 1
            else:
                myDict[num] = 1
        
        freq = [[] for _ in range(len(nums) + 1)]
        for key, value in myDict.items():
            freq[value].append(key)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for item in freq[i]:
                res.append(item)
                if len(res) == k:
                    return res
