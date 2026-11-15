class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nnums = {}
        for i in range(len(nums)):
            temp = target-nums[i]
            if temp in nnums:
                return [nnums[temp],i]
            nnums[nums[i]] = i
        return [-1, -1]

        
