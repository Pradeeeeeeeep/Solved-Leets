class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maximum = max(nums)
        ans = 0
        for i in range(len(nums)):
            ans += maximum-nums[i]
        return ans