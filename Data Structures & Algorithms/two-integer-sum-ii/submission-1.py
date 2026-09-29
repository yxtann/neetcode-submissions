class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_num = {}

        for idx, num in enumerate(nums):
            complement = target - num

            if complement in seen_num:
                # Add 1 to both indices to convert from 0-indexed to 1-indexed
                return [seen_num[complement] + 1, idx + 1]

            # Save the 0-indexed position in the dictionary for calculations
            seen_num[num] = idx