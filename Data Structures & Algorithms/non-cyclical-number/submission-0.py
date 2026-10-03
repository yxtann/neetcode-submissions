class Solution:
    def isHappy(self, n: int) -> bool:
        seen_nums = set()
        curr_num = self.square_sum(n)
        while curr_num != 1:
            if curr_num in seen_nums:
                return False
            else:
                seen_nums.add(curr_num)
                curr_num = self.square_sum(curr_num)
        return True
    
    def square_sum(self, n):
        nums = [num for num in list(str(n))]
        square_sum = 0
        for num in nums:
            square_sum += int(num)*int(num)
        return square_sum