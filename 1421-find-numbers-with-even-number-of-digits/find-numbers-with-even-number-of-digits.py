class Solution(object):
    def findNumbers(self, nums):
        even = 0
        for num in nums:
            digit= len(str(num))
            if digit % 2==0:
                even = even +1
        return even
            