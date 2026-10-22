class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_pt = 0
        right_pt = len(nums) - 1

        while left_pt <= right_pt:
            mid = (left_pt + right_pt) // 2
            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                left_pt = mid + 1
            else:
                right_pt = mid - 1

        return -1