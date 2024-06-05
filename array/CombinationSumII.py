class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        output = []
        candidates.sort()
        self.combination(candidates, target, [], output, 0, 0)
        return [list(x) for x in set(tuple(x) for x in output)]

    def combination(self, candidates, target, current_candidates, output, current_sum, index):

        if index >= len(candidates):
            if current_sum == target:
                output.append(current_candidates.copy())
            return

        if index >= len(candidates) or current_sum > target:
            return

        current_candidates.append(candidates[index])
        self.combination(candidates, target, current_candidates, output, current_sum + candidates[index], index + 1)
        current_candidates.pop()
        while index < len(candidates) - 1 and candidates[index] == candidates[index + 1]:
            index = index + 1
        self.combination(candidates, target, current_candidates, output, current_sum, index + 1)


print(Solution().combinationSum2([2, 3, 6, 7], 7))
print(Solution().combinationSum2([2, 3, 5], 8))
print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
print(Solution().combinationSum2([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 27))
