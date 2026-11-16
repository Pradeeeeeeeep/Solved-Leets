class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num]+= 1
            else:
                hashmap[num] = 1
        sorted_nums = sorted(hashmap, key=hashmap.get, reverse=True)
        return sorted_nums[:k]