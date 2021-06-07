class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        start_index = 0
        zero_index = []
        zero_count = 0
        max_length = 0
        index = -1
        for index in range(len(A)):
            if A[index] == 0:
                zero_count += 1
                zero_index.append(index)

                if zero_count == K + 1:
                    if index - start_index > max_length:
                        max_length = index - start_index
                    start_index = zero_index.pop(0) + 1
                    zero_count -= 1

        if index == len(A) - 1 and index + 1 - start_index > max_length:
            max_length = index + 1 - start_index
        return max_length


# print(Solution().longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
# print(Solution().longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))
print(Solution().longestOnes([0, 0, 0, 1], 4))
