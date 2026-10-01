class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)
        if len(list(set(nums))) != len(nums):
            return True
        else:
            return False