class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = prices[0]
        best_profit = 0

        for price in prices:
            min_price = min(price, min_price)
            best_profit = max(best_profit, price - min_price)

        return best_profit
        
