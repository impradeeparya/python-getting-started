class Solution(object):
    # def threeSum(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[List[int]]
    #     """
    #     sum_list = []
    #     for i in range(len(nums) - 2):
    #         a = nums[i]
    #         for j in range(i + 1, len(nums)):
    #             b = nums[j]
    #             for k in range(j + 1, len(nums)):
    #                 c = nums[k]
    #                 if a + b + c == 0:
    #                     temp_list = [a, b, c]
    #                     temp_list.sort()
    #                     sum_list.insert(0, temp_list)
    #                     break
    #
    #     return [list(x) for x in set(tuple(x) for x in sum_list)]

    # def threeSum(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[List[int]]
    #     """
    #     sum_list = []
    #     for i in range(len(nums) - 2):
    #         a = nums[i]
    #         unique_nums = set()
    #         for j in range(i + 1, len(nums)):
    #             b = nums[j]
    #             c = 0 - (a + b)
    #             if c in unique_nums:
    #                 temp_list = [a, b, c]
    #                 temp_list.sort()
    #                 sum_list.insert(0, temp_list)
    #             else:
    #                 unique_nums.add(b)
    #
    #     return [list(x) for x in set(tuple(x) for x in sum_list)]

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sum_list = []
        nums.sort()
        for i in range(len(nums) - 2):
            a = nums[i]
            if i > 0 and a == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1

            while l < r:
                b = nums[l]
                c = nums[r]
                if a + b + c == 0:
                    temp_list = [a, b, c]
                    temp_list.sort()
                    sum_list.insert(0, temp_list)
                    l += 1
                    r -= 1
                elif a + b + c < 0:
                    l += 1
                else:
                    r -= 1

        return [list(x) for x in set(tuple(x) for x in sum_list)]


# sum_3 = Solution().threeSum([0, 0, 0])
# sum_3 = Solution().threeSum([-1, 0, 1, 0])
sum_3 = Solution().threeSum([-1, 0, 1, 2, -1, -4])
print(sum_3)
