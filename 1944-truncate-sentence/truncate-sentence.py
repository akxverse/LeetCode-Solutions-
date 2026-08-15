class Solution(object):
    def truncateSentence(self, s, k):
        word= s.split()
        return" " .join(word[:k])