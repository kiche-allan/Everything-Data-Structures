# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)< 2:
            return 0

        min_ptr = 0
        max_ptr = 1
        max_profit = 0

        while max_ptr < len(prices):
            if prices[max_ptr] <prices[min_ptr]:
                min_ptr = max_ptr
            else:
                profit = prices[max_ptr] - prices[min_ptr]
                if profit > max_profit:
                    max_profit = profit
            max_ptr += 1
        return max_profit

#explanations
#line 8 - this is the function definition. It takes an input list of stock prices and returns an integer representing the maximum profit that can be made from buying and selling the stock.
#line 9-11 - This is a check to see if the input list contains at least two elements. If it doesn't, we can't make a profit, so we return 0.
#line 9 -15  - Here we initialize the two pointers and the maximum profit. We start with min_ptr pointing to the first element of the list, max_ptr pointing to the second element of the list, and max_profit set to 0.
# This starts a loop that will iterate through each element of the input list until max_ptr reaches the end of the list.

# This checks if the current stock price at max_ptr is lower than the minimum stock price seen so far at min_ptr. If it is, we update min_ptr to point to the new minimum stock price.

# If the current stock price at max_ptr is higher than the minimum stock price seen so far at min_ptr, we calculate the profit that could be made by selling the stock at max_ptr and buying it at min_ptr. If this profit is higher than the previous maximum profit seen so far, we update max_profit to this new value.

# This increments max_ptr by 1, moving it to the next element of the input list.

# Finally, we return the maximum profit that could be made from buying and selling the stock.


