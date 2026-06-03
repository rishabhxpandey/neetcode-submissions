class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        default is 0

        brute force:
        - basically check all pairs and see which leads to highest
        - O(n^2)

        improved:
        - when curr_profit goes down
            - move buy pointer up
        - One iteration over array

        [10,1,5,6,7,1]
        buy @ 10, sell @ 1

        if negative then move buy day up


        
        '''
        buy_ptr = 0
        curr_profit = max_profit = 0

        for sell_ptr in range(1,len(prices)):
            curr_profit = prices[sell_ptr] - prices[buy_ptr]
            max_profit = max(curr_profit, max_profit)
            if curr_profit < 0:
                buy_ptr = sell_ptr
        return max_profit