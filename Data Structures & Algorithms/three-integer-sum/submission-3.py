class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = set()
        for i in range(len(nums)):
            tgt = -nums[i]
            j = i+1
            k = len(nums)-1
            while j < k:
                if nums[j] + nums[k] < tgt:
                    j +=1
                elif nums[j] + nums[k] > tgt:
                    k -=1
                else:
                    res.add((nums[i], nums[j], nums[k]))
                    j+=1
                    k-=1
        return list(res)

