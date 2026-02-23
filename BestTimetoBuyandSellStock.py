class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p1 = 0
        p2 = 1

        last = len(prices) - 1
        max_profit = 0

        while p2 <= last:
            profit = prices[p2] - prices[p1]
            if profit > 0:
                if profit > max_profit:
                    max_profit = profit
                p2 += 1
            else:
                # if sell price better than buy price -> move buy date to sell date
                p1 = p2
                p2 += 1
        return max_profit