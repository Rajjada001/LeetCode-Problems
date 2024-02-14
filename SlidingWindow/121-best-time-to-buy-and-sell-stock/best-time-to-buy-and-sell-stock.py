class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initiate the two pointers buy and sell. 
        # Calculate the current profit and compare it with Max profit
        # Update the buy and sell pointers

        buy, sell = 0,1
        maxProfit = 0
        while sell< len(prices):
            if prices[buy]<prices[sell]:
                profit = prices[sell] - prices[buy]
                maxProfit = max(maxProfit, profit)
            else:
                buy = sell
            sell += 1
        return maxProfit
