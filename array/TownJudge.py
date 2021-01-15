class Solution(object):
    def findJudge(self, N, trust):
        if N == 1:
            return 1

        trustWorthy = {}

        for index in range(len(trust)):
            pair = trust[index]
            worthies = trustWorthy.get(pair[1])
            if worthies is None:
                worthies = 1
                trustWorthy[pair[1]] = worthies
            else:
                worthies += 1
                trustWorthy[pair[1]] = worthies

        judge_found = False
        judge = None
        for key, value in trustWorthy.items():
            if value == N - 1:
                if judge_found:
                    judge_found = False
                    break
                else:
                    judge_found = True
                    judge = key

        if not judge_found:
            return -1

        judge_trust_others = False
        for index in range(len(trust)):
            pair = trust[index]
            if pair[0] == judge:
                judge_trust_others = True
                break

        return -1 if judge_trust_others else judge


print(Solution().findJudge(2, [[1, 2]]))
print(Solution().findJudge(3, [[1, 3], [2, 3]]))
print(Solution().findJudge(3, [[1, 3], [2, 3], [3, 1]]))
print(Solution().findJudge(3, [[1, 2], [2, 3]]))
print(Solution().findJudge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]))
print(Solution().findJudge(1, []))
