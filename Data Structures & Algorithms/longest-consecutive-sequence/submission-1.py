class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # find possible starting numbers
        myset = set(nums)
        starters = []
        for num in nums:
            if num-1 not in myset:
                starters.append(num)
        
        # find length of consecutive sequences
        lengths = []
        for start in starters:
            c = 0
            while start in myset:
                c+=1
                start+=1
            lengths.append(c)
        return max(lengths)