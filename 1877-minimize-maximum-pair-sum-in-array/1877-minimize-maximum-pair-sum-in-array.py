class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        right = 0
        left = len(nums)-1
        ans = 0
        while(right<left):
            ans = max((sorted_nums[right]+sorted_nums[left]), ans)
            right+=1
            left-=1
        return ans