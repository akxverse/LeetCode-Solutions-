class Solution(object):
    def countCommas(self, n):
        count=0
        '''for i in range(1, n+1):
            if i>= 1000:
                count +=1
        return count'''
        if n < 1000:
                return 0
        else:
            return n - 1000 + 1
       
        