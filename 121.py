class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buying_price = float('inf')
        best_profit = 0
        for price in prices:
            if min_buying_price < price:
                profit = price - min_buying_price
                if profit > best_profit:
                    best_profit = profit
            else:
                min_buying_price = price
            
        return best_profit
