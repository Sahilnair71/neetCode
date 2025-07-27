# question:
# You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

# You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

# Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

# Solution Conplexit:
# Time complexity: O(n)
# Space Complexity: O(1)



class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy_price = prices[0]
        profit=0
        for sell_price in prices:

            profit=max(profit,sell_price - buy_price)
            buy_price=min(buy_price,sell_price)
        return profit