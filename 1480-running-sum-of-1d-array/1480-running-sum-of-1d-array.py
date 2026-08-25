class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        currentSum = nums[0]
        i=1
        while(i<len(nums)):
            currentSum += nums[i]
            nums[i] = currentSum
            i+=1

        return nums
        