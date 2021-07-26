from typing import List


class Solution:
    def knapsack(self, price: List[int], weights: List[int], weight: int, index: int, memory: List[List[int]]):
        if weight == 0 or index == 0:
            return 0

        if memory[index][weight] == -1:

            if weights[index - 1] <= weight:
                memory[index][weight] = max(
                    price[index - 1] + self.knapsack(price, weights, weight - weights[index - 1], index - 1, memory),
                    self.knapsack(price, weights, weight, index - 1, memory))

            if weights[index - 1] > weight:
                memory[index][weight] = self.knapsack(price, weights, weight, index - 1, memory)

        return memory[index][weight]


memory = [[-1 for row in range(0, 10)] for column in range(0, 10)]
print(Solution().knapsack([1, 4, 5, 7], [1, 3, 4, 5], 7, 4, memory))
