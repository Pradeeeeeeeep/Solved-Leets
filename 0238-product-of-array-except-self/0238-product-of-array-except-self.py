class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]
        
        for i in range(1, len(nums)):
            ans.append(ans[i-1] * nums[i-1])
        suffix = 1
        for j in range(len(nums)-1, -1, -1):
            ans[j]*=suffix
            suffix*=nums[j]
        return ans