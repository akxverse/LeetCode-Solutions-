class Solution(object):
    def shuffle(self, nums, n):
        array=[]
        for i in range(n):
            array.extend([nums[i],nums[i+n]])
            '''array.append (nums[i])
            array.append(nums[i+n])'''
        return array