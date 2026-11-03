class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        target_sum = threshold*k
        window_sum = sum(arr[:k])
        ans = 0
        if window_sum>=target_sum:
            ans+=1
        for right in range(k,len(arr)):
            window_sum+=arr[right]
            window_sum-=arr[right-k]
            if window_sum>=target_sum:
                ans+=1
        return ans