class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        max_val = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                p = prices[r] - prices[l]
                if p > max_val:
                    max_val = p
            else:
                l = r
            r+=1
            
                
        
        return max_val

