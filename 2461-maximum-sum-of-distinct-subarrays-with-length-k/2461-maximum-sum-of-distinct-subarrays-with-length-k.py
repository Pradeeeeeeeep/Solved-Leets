class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq = {}
        l = 0
        summ = 0
        ans = 0

        for r in range(len(nums)):
            summ += nums[r]
            freq[nums[r]] = freq.get(nums[r], 0) + 1
            if r - l + 1 > k:
                freq[nums[l]] -= 1
                if freq[nums[l]] == 0:
                    del freq[nums[l]]
                summ -= nums[l]
                l += 1

            if r - l + 1 == k and len(freq) == k:
                ans = max(ans, summ)

        return ans