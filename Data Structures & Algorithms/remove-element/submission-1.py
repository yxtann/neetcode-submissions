class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        elem_counter = 0
        for i, num in enumerate(nums):
            if num == val:
                nums[i] = 10000
                elem_counter += 1
        
        nums.sort()
        
        return len(nums) - elem_counter

        