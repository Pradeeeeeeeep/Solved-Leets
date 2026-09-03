class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, area = 0, len(height)-1, 0
        while l<r:
            w = r-l
            h = min(height[r], height[l])
            temp = w*h
            area = max(area, temp)
            if height[l] < height[r]: l += 1
            else: r -= 1
        return area