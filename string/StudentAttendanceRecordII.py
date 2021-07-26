# An attendance record for a student can be represented as a string where each character signifies whether the
# student was absent, late, or present on that day. The record only contains the following three characters:
#
# 'A': Absent.
# 'L': Late.
# 'P': Present.
# Any student is eligible for an attendance award if they meet both of the following criteria:
#
# The student was absent ('A') for strictly fewer than 2 days total. The student was never late ('L') for 3 or more
# consecutive days. Given an integer n, return the number of possible attendance records of length n that make a
# student eligible for an attendance award. The answer may be very large, so return it modulo 109 + 7.


class Solution:

    # def allowed_awardee(self, attendance):
    #     is_awardee_allowed = True
    #     absent_count = 0
    #     leave_count = 0
    #     for attendance_mark in attendance:
    #         if attendance_mark == 'A':
    #             absent_count = absent_count + 1
    #             leave_count = 0
    #         elif attendance_mark == 'L':
    #             leave_count = leave_count + 1
    #         else:
    #             leave_count = 0
    #
    #         if absent_count >= 2 or leave_count >= 3:
    #             is_awardee_allowed = False
    #     return is_awardee_allowed

    def awardees_count(self, attendance, attendance_markers, total_attendance, absent_count, leave_count):

        awardees_count = 0
        if absent_count < 2 and leave_count < 3:
            if len(attendance) == total_attendance:
                return 1

            for attendance_marker in attendance_markers:
                awardees_count = awardees_count + self.awardees_count(attendance + attendance_marker,
                                                                      attendance_markers,
                                                                      total_attendance,
                                                                      absent_count + 1 if attendance_marker == 'A' else absent_count,
                                                                      leave_count + 1 if attendance_marker == 'L' else 0)

        return awardees_count

    def checkRecord(self, n: int) -> int:
        attendance_markers = ['A', 'L', 'P']
        return self.awardees_count('', attendance_markers, n, 0, 0)


print(Solution().checkRecord(n=2))
print(Solution().checkRecord(n=1))
print(Solution().checkRecord(n=10101))
