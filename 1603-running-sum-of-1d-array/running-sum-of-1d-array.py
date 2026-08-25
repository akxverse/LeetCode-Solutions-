class Solution(object):
    def runningSum(self, nums):
        #1d array
        for i in range (1, len(nums)):
            nums[i]= nums[i]+ nums[i-1]
        return nums
