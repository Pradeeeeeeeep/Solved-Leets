class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        ans = 0
        window_sum = sum(arr[:k])
        window_avg = window_sum/k
        if window_avg >= threshold:
            ans+=1
        for right in range(k,len(arr)):
            window_sum+=arr[right]
            window_sum-=arr[right-k]
            window_avg = window_sum/k
            if window_avg >= threshold:
                ans+=1
        return ans