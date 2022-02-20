class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        agni = {}
        for item in nums:
            if item in agni:
                return True
            else:
                agni[item] = 1
        return False
