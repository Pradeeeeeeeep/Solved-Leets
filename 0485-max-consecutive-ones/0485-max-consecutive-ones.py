class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOne=count=0
        for num in nums:
            if num:
                count+=1
            else:
                maxOne=count if maxOne<count else maxOne
                count = 0
            
        return max(maxOne, count)