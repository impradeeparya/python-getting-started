class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        length_nums1 = len(nums1)
        length_nums2 = len(nums2)

        is_even = True if (length_nums1 + length_nums2) % 2 == 0 else False

        if is_even:
            median_index1 = int(((length_nums1 + length_nums2 + 1) / 2) - 1)
            median_index2 = median_index1 + 1
            median1 = None
            median2 = None
            nums1_index = 0
            nums2_index = 0
            for index in range(length_nums1 + length_nums2):
                if nums1_index < length_nums1 and nums2_index < length_nums2:
                    if nums1[nums1_index] <= nums2[nums2_index]:
                        median = nums1[nums1_index]
                        nums1_index += 1
                    else:
                        median = nums2[nums2_index]
                        nums2_index += 1
                elif nums1_index < length_nums1:
                    median = nums1[nums1_index]
                    nums1_index += 1
                else:
                    median = nums2[nums2_index]
                    nums2_index += 1

                if index == median_index1:
                    median1 = median

                if index == median_index2:
                    median2 = median
                    return (median1 + median2) / 2
        else:
            median_index = int(((length_nums1 + length_nums2 + 1) / 2) - 1)
            nums1_index = 0
            nums2_index = 0
            for index in range(length_nums1 + length_nums2):
                if nums1_index < length_nums1 and nums2_index < length_nums2:
                    if nums1[nums1_index] <= nums2[nums2_index]:
                        median = nums1[nums1_index]
                        nums1_index += 1
                    else:
                        median = nums2[nums2_index]
                        nums2_index += 1
                elif nums1_index < length_nums1:
                    median = nums1[nums1_index]
                    nums1_index += 1
                else:
                    median = nums2[nums2_index]
                    nums2_index += 1

                if index == median_index:
                    return median


nums1 = [1, 2]
nums2 = [3, 4]
array_median = Solution().findMedianSortedArrays(nums1, nums2)
print(array_median)
