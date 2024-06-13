class Solution(object):
    def smallestRangeI(self, nums, k):
        
        max_val = max(nums)
        min_val = min(nums)

        variable_1 = max_val - k
        variable_2 = min_val + k

        if variable_2 > variable_1:
            return 0
        else:
            return variable_1 - variable_2


