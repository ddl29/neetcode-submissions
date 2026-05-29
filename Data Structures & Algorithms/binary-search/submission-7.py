class Solution:
    def search(self, nums: List[int], target: int) -> int:
        size = len(nums)
        left = 0
        right = math.ceil(size/2)

        while left < right and right <= size:
            for i in range(left, right):
                if nums[i] == target:
                    return i
            dif = right - left
            left = right
            right += math.ceil(dif/2)
        return -1
