class Solution(object):
    def truncateSentence(self, s, k):
        #truncate sentence 
        word= s.split()
        return" " .join(word[:k]) 
        