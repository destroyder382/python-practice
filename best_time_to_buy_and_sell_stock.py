# LeetCode 121. Best Time to Buy and Sell Stock
# Дан массив цен по дням, найти максимальную прибыль от одной покупки и одной
# продажи (продажа обязательно позже покупки).

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = 10000000
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                diff = price - min_price
                if diff > max_profit:
                    max_profit = diff
        return max_profit
