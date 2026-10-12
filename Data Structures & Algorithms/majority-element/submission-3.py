class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj_num = nums[0]
        vote = 0

        for num in nums:

            # Reset the candidate
            if vote == 0: 
                maj_num = num

            if num == maj_num:
                vote += 1
            else:
                vote -= 1
        
        return maj_num