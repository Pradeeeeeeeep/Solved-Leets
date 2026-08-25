class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        count = {}
        output = []
        for i in range(len(sorted_nums)):
            if sorted_nums[i] not in count:
                count[sorted_nums[i]] = i
        for i in nums:
            output.append(count[i])
        return output
