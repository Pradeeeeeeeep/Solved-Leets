class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        for i in range(len(nums)):
            left = max(nums[0:i+1])
            right = min(nums[i:len(nums)])

            ans = left-right
            if ans<=k:
                return i
        return -1