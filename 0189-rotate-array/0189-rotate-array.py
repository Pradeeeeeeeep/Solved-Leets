class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        k=k%len(nums)
        
        x=nums[len(nums)-k:]
        del nums[len(nums)-k:len(nums)]
        nums[0:0]=x