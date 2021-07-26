# Given an array of unique integers salary where salary[i] is the salary of the employee i.
#
# Return the average salary of employees excluding the minimum and maximum salary.
from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        sal_sum = 0
        min_sal = salary[0] if salary[0] < salary[1] else salary[1]
        max_sal = salary[1] if salary[1] > salary[0] else salary[0]
        for index in range(2, len(salary)):

            if min_sal > salary[index]:
                sal_sum = sal_sum + min_sal
                min_sal = salary[index]
            elif max_sal < salary[index]:
                sal_sum = sal_sum + max_sal
                max_sal = salary[index]
            else:
                sal_sum = sal_sum + salary[index]

        return sal_sum / (len(salary) - 2)


print(Solution().average([4000, 3000, 1000, 2000]))
