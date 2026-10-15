class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        read_pointer = 1
        write_pointer = 1

        if len(nums) == 0:
            return

        for num in nums[1:]:
            if nums[read_pointer] == nums[read_pointer - 1]:
                read_pointer += 1
            else:
                nums[write_pointer] = num
                write_pointer += 1
                read_pointer += 1

        return write_pointer
