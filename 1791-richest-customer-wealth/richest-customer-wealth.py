class Solution(object):
    def maximumWealth(self, accounts):
        maximum=0
        for account in accounts:
            total = sum(account)
            if total> maximum:
                maximum =total
        return maximum 