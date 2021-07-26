# LeetCode company workers use key-cards to unlock office doors. Each time a worker uses their key-card, the security
# system saves the worker's name and the time when it was used. The system emits an alert if any worker uses the
# key-card three or more times in a one-hour period.
#
# You are given a list of strings keyName and keyTime where [keyName[i], keyTime[i]] corresponds to a person's name
# and the time when their key-card was used in a single day.
#
# Access times are given in the 24-hour time format "HH:MM", such as "23:51" and "09:49".
#
# Return a list of unique worker names who received an alert for frequent keycard use. Sort the names in ascending
# order alphabetically.
#
# Notice that "10:00" - "11:00" is considered to be within a one-hour period, while "22:51" - "23:52" is not
# considered to be within a one-hour period.
from typing import List


class Solution:

    def alert_count(self, key_time):
        key_time.sort()
        # print(key_time)
        start_time_values = key_time[0].split(':')
        n = len(key_time)
        start_index = 0
        count = 1
        index = 1
        while index < n:
            start_time_hr = int(start_time_values[0])
            start_time_min = int(start_time_values[1])

            current_time_values = key_time[index].split(':')
            current_time_hr = int(current_time_values[0])
            current_time_min = int(current_time_values[1])

            if current_time_hr - start_time_hr == 0:
                count = count + 1
                index = index + 1
            elif current_time_hr - start_time_hr == 1:
                total_minutes = 0
                if start_time_min == 0 and current_time_min == 0:
                    total_minutes = current_time_min
                elif start_time_min == 0:
                    total_minutes = 61
                else:
                    total_minutes = current_time_min + (60 - start_time_min)

                if total_minutes <= 60:
                    count = count + 1
                    index = index + 1
                else:
                    count = 1
                    start_index = start_index + 1
                    start_time_values = key_time[start_index].split(':')
                    index = start_index + 1

            else:
                count = 1
                start_index = start_index + 1
                start_time_values = key_time[start_index].split(':')
                index = start_index + 1

            if count >= 3:
                break

        return count

    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:

        n = len(keyName)

        swipe_details = {}
        for index in range(n):
            swipe_detail = swipe_details.get(keyName[index], None)

            if swipe_detail is None:
                swipe_detail = [keyTime[index]]
            else:
                swipe_detail.append(keyTime[index])
            swipe_details[keyName[index]] = swipe_detail

        names = []
        for key, value in swipe_details.items():
            # print(key, end=" ")
            if self.alert_count(value) >= 3:
                names.append(key)

        names.sort()
        return names


print("output ['daniel'] ",
      Solution().alertNames(keyName=["daniel", "daniel", "daniel", "luis", "luis", "luis", "luis"],
                            keyTime=["10:00", "10:40", "11:00", "09:00", "11:00", "13:00", "15:00"]))
print("output [] ", Solution().alertNames(keyName=["a", "a", "a", "a", "b", "b", "b", "b", "c", "c", "c", "c"],
                                          keyTime=["16:35", "08:13", "03:14", "15:33", "11:59", "09:25", "11:11",
                                                   "08:42",
                                                   "21:20",
                                                   "12:15",
                                                   "15:05", "03:39"]))
print("output ['bob'] ", Solution().alertNames(keyName=["alice", "alice", "alice", "bob", "bob", "bob", "bob"],
                                               keyTime=["12:01", "12:00", "18:00", "21:00", "21:20", "21:30", "23:00"]))
print("output [] ", Solution().alertNames(keyName=["john", "john", "john"], keyTime=["23:58", "23:59", "00:01"]))
print("output ['clare','leslie] ",
      Solution().alertNames(keyName=["leslie", "leslie", "leslie", "clare", "clare", "clare", "clare"],
                            keyTime=["13:00", "13:20", "14:00", "18:00", "18:51", "19:30", "19:49"]))
print("output ['a] ", Solution().alertNames(keyName=["a", "a", "a", "a", "a", "a", "b", "b", "b", "b", "b"],
                                            keyTime=["23:27", "03:14", "12:57", "13:35", "13:18", "21:58", "22:39",
                                                     "10:49", "19:37",
                                                     "14:14", "10:41"]))
print("output ['d'] ", Solution().alertNames(
    keyName=["a", "a", "a", "b", "b", "b", "b", "b", "b", "b", "c", "c", "c", "c", "c", "c", "c", "d", "d", "d", "d",
             "d", "d", "d"],
    keyTime=["13:14", "12:21", "14:32", "04:10", "01:36", "13:06", "23:55", "09:33", "20:39", "15:47", "01:57", "16:43",
             "20:33", "08:42", "06:05", "21:56", "17:12", "20:41", "19:53", "20:13", "02:49", "18:56", "16:48",
             "08:37"]))

print("output [] ", Solution().alertNames(
    keyName=["a", "a", "a", "a", "a", "a", "b", "b", "b", "b", "b", "b", "b", "c", "c", "c", "c", "c", "d", "d", "d",
             "d", "d", "e", "e", "e", "e", "e", "f", "f", "f", "f", "f", "g", "g", "g", "g", "g", "g", "g", "h", "h",
             "h", "h", "h", "i", "i", "i", "i", "i", "i", "i", "i", "j", "j", "j", "j", "j", "j", "j", "k", "k", "k",
             "k", "k", "k", "k", "k", "l", "l", "l", "l", "l", "l", "l", "m", "m", "m", "m", "m", "m", "n", "n", "n",
             "n", "n", "n", "o", "o", "o", "o", "o", "o", "o", "p", "p", "p", "p", "p", "p", "p", "q", "q", "q", "q",
             "q", "q", "q", "r", "r", "r", "r", "r", "s", "s", "s", "s", "s", "s", "t", "t", "t", "t", "t"],
    keyTime=["08:32", "12:34", "02:08", "14:18", "16:51", "06:37", "13:15", "19:23", "22:42", "11:53", "08:32", "07:23",
             "01:14", "18:17", "22:59", "12:24", "07:26", "10:07", "00:52", "08:37", "20:28", "21:53", "02:45", "00:36",
             "13:07", "09:58", "04:03", "14:35", "03:48", "22:23", "03:42", "00:48", "00:47", "21:18", "06:51", "14:41",
             "20:18", "17:04", "09:33", "12:09", "04:52", "07:27", "20:02", "23:45", "02:00", "22:54", "16:18", "05:51",
             "02:45", "18:27", "10:59", "14:34", "18:41", "15:28", "23:52", "21:04", "03:56", "08:02", "03:03", "08:10",
             "14:00", "06:27", "00:02", "15:33", "02:38", "17:18", "20:14", "08:59", "11:18", "08:56", "19:15", "23:41",
             "22:51", "10:17", "07:12", "06:21", "15:46", "01:28", "15:05", "05:41", "21:52", "04:45", "10:26", "04:37",
             "15:00", "16:27", "16:56", "03:18", "23:22", "13:18", "10:13", "19:15", "02:45", "06:53", "12:34", "15:32",
             "18:12", "18:16", "08:37", "04:51", "22:23", "12:03", "21:10", "16:44", "11:44", "21:13", "19:14", "03:56",
             "05:28", "13:31", "09:12", "11:23", "02:45", "21:50", "06:40", "02:56", "23:06", "00:25", "14:05", "17:03",
             "13:33", "18:08", "13:11", "16:36"]))
