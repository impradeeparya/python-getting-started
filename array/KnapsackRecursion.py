from typing import List


class Solution:
    def knapsack(self, price: List[int], weights: List[int], weight: int, index: int):
        if weight == 0 or index == 0:
            return 0

        if weights[index - 1] <= weight:
            return max(price[index - 1] + self.knapsack(price, weights, weight - weights[index - 1], index - 1),
                       self.knapsack(price, weights, weight, index - 1))

        if weights[index - 1] > weight:
            return self.knapsack(price, weights, weight, index - 1)


print(Solution().knapsack([1, 4, 5, 7], [1, 3, 4, 5], 7, 4))
