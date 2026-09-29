class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num_one_idx, num_one in enumerate(nums):
            num_one = nums[num_one_idx]

            for num_two_idx, num_two in enumerate(nums[num_one_idx+1:]):

                if num_one + num_two == target:
                    num_two_idx = num_one_idx + 1 + num_two_idx
                    return [num_one_idx, num_two_idx]