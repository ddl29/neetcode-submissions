class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}
        for i, num in enumerate(nums):
            if num in myDict:
                print(myDict[num])
                return [myDict[num], i]
            else:
                myDict[target - num] = i
                