class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp = list(nums)
        nums.sort(reverse=True)
        count = {}
        index = 0
        while index < len(nums):
            value = nums[index]
            index = index + 1
            while index < len(nums) and value == nums[index]:
                index = index + 1

            if index < len(nums):
                count[value] = (len(nums) - index)
            else:
                count[value] = 0

        return [count[element] for element in temp]


print(Solution().smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
