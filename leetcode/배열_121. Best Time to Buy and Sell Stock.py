from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        INF = int(1e9)
        profit = 0
        min_price = INF
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
        return profit