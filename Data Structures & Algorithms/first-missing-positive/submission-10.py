class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        # Do partial sort TODO: step throug hthis
        for i, num in enumerate(nums):
            # keep swapping until all numbers are in their home position
            while 0 < nums[i] <= len(nums) and nums[nums[i]-1] != nums[i]:
                home = nums[i] - 1 # home index for the current element at i
                nums[i], nums[home] = nums[home], nums[i]

        # Check if i is not num, then we have the first missing positive
        for i, num in enumerate(nums):
            if i+1 != num:
                return i+1
        
        return len(nums) + 1
