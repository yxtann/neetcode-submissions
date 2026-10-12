class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        w = 0

        for i, num in enumerate(nums):
            if num != val:
               nums[w] = nums[i]
               w += 1
            
        return w

        