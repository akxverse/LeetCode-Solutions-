class Solution(object):
    def maxProduct(self, nums):
        i = max(nums)
        nums.remove(i)
        j= max(nums)
        
        return (i-1)* (j-1)
        