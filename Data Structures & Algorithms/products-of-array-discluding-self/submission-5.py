class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #                [ 1, 2, 4, 6]
        # prefix product [ 1, 2, 8,48]
        # suffix product [48,48,24, 6]

        # prefix[i]/i = 2
        # suffix[i]/i = 6

        prefix = [1]
        suffix = [1]
        
        p = 1
        for i in range(1, len(nums)):
            p *= nums[i-1]
            prefix.append(p)
        
        # [24,24,6,1]
        p = 1
        for i in range(len(nums)-1, 0, -1):
            p *= nums[i]
            suffix.append(p)
        suffix.reverse()

        res = []
        for i in range(len(nums)):
            res.append(prefix[i] * suffix[i])
        return res
