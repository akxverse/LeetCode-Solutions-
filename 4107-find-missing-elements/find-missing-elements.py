class Solution(object):
    def findMissingElements(self, nums):
        array=[]
        for i in range(min(nums),max(nums)):
            if i not in nums:
                array.append(i)
        return array