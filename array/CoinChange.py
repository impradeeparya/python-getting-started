class Solution:
    def process_coin(self, coins, m, amount, outputs, count):
        if amount == 0:
            outputs.append(count)
            return
        if amount < 0 or m < 0:
            return

        self.process_coin(coins, m, amount - coins[m], outputs, count + 1)
        self.process_coin(coins, m - 1, amount, outputs, count)

    # def coinChange(self, coins, amount):
    #     """
    #     :type coins: List[int]
    #     :type amount: int
    #     :rtype: int
    #     """
    #     output = -1
    #     outputs = []
    #     m = len(coins) - 1
    #     count = 0
    #     self.process_coin(coins, m, amount - coins[m], outputs, count + 1)
    #     self.process_coin(coins, m - 1, amount, outputs, count)
    #
    #     for index in range(len(outputs)):
    #         if (output == -1) or (outputs[index] < output):
    #             output = outputs[index]
    #
    #     return output

    def coinChange(self, coins, amount):
        if amount <= 0:
            return 0
        table = [[0 for column in range(amount + 1)] for row in range(len(coins))]
        for row in range(len(coins)):
            for column in range(1, amount + 1):
                amount_left = column - coins[row]
                if amount_left < 0:
                    table[row][column] = table[row - 1][column] if row - 1 >= 0 else 0
                elif amount_left > 0:
                    table[row][column] = table[row][amount_left] + 1 if table[row][amount_left] > 0 else 0
                else:
                    table[row][column] = 1
        return table[len(coins) - 1][amount] if table[len(coins) - 1][amount] > 0 else -1


# print(Solution().coinChange([1, 2, 5], 11))
# print(Solution().coinChange([2], 3))
print(Solution().coinChange([1], 0))
