class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left_only_prod = [1] * len(nums)
        right_only_prod = [1] * len(nums)
        product_except_self = []

        # build left_only_prod
        # left_only_prod[i] = product of everything strictly BEFORE i,
        # i.e. nums[0] * ... * nums[i-1]. Each slot excludes its own number.
        #
        # To fill slot i, reuse the previous slot:
        #   left_only_prod[i-1] = nums[0] * ... * nums[i-2]  (stops just short)
        #   nums[i-1]           = the one number it stopped short of
        # Multiplying them fills the gap -> nums[0] * ... * nums[i-1].
        # Both use i-1: the running total, and the number it left out.
        #
        # Slot 0 has nothing before it, so it's the "empty product" = 1.
        for i, num in enumerate(nums):
            if i == 0:
                left_only_prod[i] = 1
            else:
                left_only_prod[i] = nums[i-1] * left_only_prod[i-1]

        # build right_only_prod
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums) - 1:
                right_only_prod[i] = 1
            else:
                right_only_prod[i] = nums[i+1] * right_only_prod[i+1]

        # answer[i] = (everything before i) * (everything after i)
        for num_1, num_2 in zip(left_only_prod, right_only_prod):
            product_except_self.append(num_1 * num_2)

        return product_except_self