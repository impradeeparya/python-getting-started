from typing import List


class Solution:
    def knapsack(self, price: List[int], weights: List[int], weight: int):
        elements = len(price)
        memory = [[0 for column in range(weight + 1)] for column in range(elements + 1)]

        for row in range(1, elements + 1):
            for column in range(1, weight + 1):
                if weights[row - 1] <= column:
                    memory[row][column] = max(price[row - 1] + memory[row - 1][column - weights[row - 1]],
                                              memory[row - 1][weight])
                else:
                    memory[row][column] = memory[row - 1][column]

        print(memory)
        return memory[elements][weight]


print(Solution().knapsack([1, 4, 5, 7], [1, 3, 4, 5], 7))
