class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        output = []
        self.combination(candidates, target, [], output, 0, 0)
        return [list(x) for x in set(tuple(x) for x in output)]

    def combination(self, candidates, target, current_candidates, output, current_sum, index):

        if current_sum == target:
            output.append(current_candidates.copy())
        elif current_sum < target:
            for i in range(index, len(candidates)):
                current_candidates.append(candidates[i])
                self.combination(candidates, target, current_candidates, output, current_sum + candidates[i], i)
                current_candidates.pop()


print(Solution().combinationSum([2, 3, 6, 7], 7))
print(Solution().combinationSum([2, 3, 5], 8))
print(Solution().combinationSum([10, 1, 2, 7, 6, 1, 5], 8))
