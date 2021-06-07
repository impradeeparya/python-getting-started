class Solution:
    def is_ascending(self, prices):
        is_ascending = True

        for index in range(1, len(prices)):
            if prices[index] < prices[index - 1]:
                is_ascending = False
                break
        return is_ascending

    def is_descending(self, prices):
        is_descending = True

        for index in range(1, len(prices)):
            if prices[index] > prices[index - 1]:
                is_descending = False
                break
        return is_descending

    # def maxProfit(self, prices):
    #     max_profile = None
    #
    #     if self.is_ascending(prices):
    #         max_profile = prices[len(prices) - 1] - prices[0]
    #     elif self.is_descending(prices):
    #         max_profile = 0
    #     else:
    #         for row in range(len(prices) - 1):
    #             for column in range(row + 1, len(prices)):
    #                 buy = prices[row]
    #                 sell = prices[column]
    #                 if buy < sell:
    #                     if max_profile is None or max_profile < (sell - buy):
    #                         max_profile = sell - buy
    #
    #     return max_profile if max_profile is not None else 0

    def maxProfit(self, prices):
        max_profit = 0
        min_prices = [0] * len(prices)
        current_min = prices[0]
        min_prices[0] = current_min
        for index in range(1, len(prices)):
            if current_min > prices[index]:
                current_min = prices[index]
            min_prices[index] = current_min

        max_prices = [0] * len(prices)
        current_max = prices[len(prices) - 1]
        max_prices[len(prices) - 1] = current_max
        for index in range(len(prices) - 2, -1, -1):
            if current_max < prices[index]:
                current_max = prices[index]
            max_prices[index] = current_max

        for index in range(len(prices)):
            buy = min_prices[index]
            sell = max_prices[index]
            if buy < sell:
                if max_profit < (sell - buy):
                    max_profit = sell - buy
        return max_profit


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
