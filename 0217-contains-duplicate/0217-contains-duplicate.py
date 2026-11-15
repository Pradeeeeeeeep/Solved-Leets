class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        temp = {}
        for i in range(len(nums)):
            if nums[i] in temp:
                return True
            temp[nums[i]] = nums[i]
        return False