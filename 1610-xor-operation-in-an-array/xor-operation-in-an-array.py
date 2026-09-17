class Solution(object):
    def xorOperation(self, n, start):
        num=0
        for i in range (n):
            num = num^ (start +2*i)
        return num

        