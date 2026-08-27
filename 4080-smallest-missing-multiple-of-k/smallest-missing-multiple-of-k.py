class Solution(object):
    def missingMultiple(self, nums, k):
       x=k
       while x in nums:
        x= x+k
       return x
        