class Solution:
    def countElements(self, nums: list[int]) -> int:
        arrMin = min(nums)
        arrMax = max(nums)
        ans = 0
        for num in nums:
            if num != arrMin and num != arrMax:
                ans+=1
        return ans