class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_num = {}
        for idx, num in enumerate(nums):
            if (target - num) in seen_num:
                # return what we saw in the past, and the curr num idx
                return [seen_num[target - num], idx]
            seen_num[num] = idx