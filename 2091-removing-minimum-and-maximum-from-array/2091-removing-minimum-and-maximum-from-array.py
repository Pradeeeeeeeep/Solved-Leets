class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        min_pos = nums.index(min(nums)) + 1
        max_pos = nums.index(max(nums)) + 1
        
        left = min(min_pos, max_pos)
        right = max(min_pos, max_pos)

        remove_left = right
        remove_right = n - left + 1
        remove_both = left + (n - right + 1)

        return min(remove_left, remove_right, remove_both)