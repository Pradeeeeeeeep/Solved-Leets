class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best = 0
        run = 0
        i=0
        while i<len(nums):
            if nums[i]==1:
                run+=1
            else:
                best = max(run, best)
                run=0
            i+=1
        best = max(run, best)
        return best