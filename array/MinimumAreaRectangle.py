# Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points,
# with sides parallel to the x and y axes.
#
# If there isn't any rectangle, return 0.
from typing import List


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        coordinates = {}
        for point in points:
            x = point[0]
            y = point[1]
            if coordinates.get(x, None) is None:
                coordinates[point[0]] = {y:True}
            else:
                coordinates[x][y] = True

        min_area = 0
        n = len(points)

        for index in range(n):
            for sub_index in range(index+1, n):

                x1 = points[index][0]
                y1 = points[index][1]

                x2 = points[sub_index][0]
                y2 = points[sub_index][1]

                if x1 != x2 and y1 != y2:
                    if coordinates.get(x2).get(y1, None) is not None and coordinates.get(x1).get(y2, None) is not None:
                        area = abs(x2-x1) * abs(y2-y1)
                        if area < min_area or min_area == 0:
                            min_area = area

        return min_area


print("output 4 ", Solution().minAreaRect([[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]))
print("output 2 ", Solution().minAreaRect([[1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3]]))
