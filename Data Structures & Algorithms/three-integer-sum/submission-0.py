class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution = []
        nums = sorted(nums)

        for i, fixed_num in enumerate(nums):

            # If the fixed number is the same as its neighbors, we will just keep searching its neighbors
            # until its next neighbor is a different value
            if i != 0:
                if nums[i-1] == fixed_num:
                    continue
                
            trunc_nums = nums[i+1:]
            left_pointer = 0
            right_pointer = len(trunc_nums) - 1

            while left_pointer < right_pointer:
                left_val = trunc_nums[left_pointer]
                right_val = trunc_nums[right_pointer]
                curr_sum = fixed_num + left_val + right_val
                
                if curr_sum == 0:
                    solution.append([fixed_num, left_val, right_val])
                    left_pointer += 1
                    # Skip duplicate by just moving the left pointer
                    while left_pointer < right_pointer and trunc_nums[left_pointer] == trunc_nums[left_pointer - 1]:
                        left_pointer += 1
                if curr_sum > 0:
                    right_pointer -= 1
                if curr_sum < 0:
                    left_pointer += 1
            
        return solution
