class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest_sum = None
        for i in range(len(nums)):
            a = nums[i]
            if i > 0 and a == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1

            while l < r:
                b = nums[l]
                c = nums[r]
                target_sum = a + b + c

                if closest_sum is None:
                    closest_sum = target - target_sum
                else:
                    closest_sum = closest_sum if abs(closest_sum) < abs(target - target_sum) else target - target_sum

                if target_sum < target:
                    l += 1
                else:
                    r -= 1
            if closest_sum == 0:
                break
        return target - closest_sum

    def threeSumClosest1(self, nums, target):
        diff = float('inf')
        nums.sort()
        for i in range(len(nums)):
            lo, hi = i + 1, len(nums) - 1
            while (lo < hi):
                sum = nums[i] + nums[lo] + nums[hi]
                if abs(target - sum) < abs(diff):
                    diff = target - sum
                if sum < target:
                    lo += 1
                else:
                    hi -= 1
            if diff == 0:
                break
        return target - diff


sum_closest = Solution().threeSumClosest([-1, 2, 1, -4], 1)
print(sum_closest)
