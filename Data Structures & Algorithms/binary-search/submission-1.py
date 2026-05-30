class Solution:
    def search(self, nums: List[int], target: int) -> int:
        size = len(nums)
        
        left = 0
        right = size -1

        while left <= right:
            half = (left + right) //2
            if nums[half] == target:
                return half
            else:
                if target < nums[half]:
                    right = half -1
                else:
                    left = half + 1
        return -1