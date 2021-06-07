#
# Complete the 'droppedRequests' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY requestTime as parameter.
#

def droppedRequests(requestTime):
    # Write your code here
    total_10_sec_request_count = 0
    total_59_sec_request_count = 0
    drop_count = 0
    request_time_frequency = {}
    window = [requestTime[0]]
    window_10_sec_start_index = 0
    window_59_sec_start_index = 0
    window_index = 0
    for index in range(len(requestTime)):
        current_count = request_time_frequency.get(requestTime[index], None)
        total_10_sec_request_count += 1
        total_59_sec_request_count += 1

        if window[window_index] != requestTime[index]:
            window.append(requestTime[index])
            window_index += 1

        if window[window_index] - window[window_10_sec_start_index] > 9:
            prev_start_index = window_10_sec_start_index
            while window[window_index] - window[window_10_sec_start_index] > 9:
                print(window_10_sec_start_index, window_index)
                window_10_sec_start_index += 1
            for time in range(prev_start_index, window_10_sec_start_index):
                request_count = request_time_frequency.get(window[time], None)
                total_10_sec_request_count -= request_count

        if window[window_index] - window[window_59_sec_start_index] > 59:
            prev_start_index = window_59_sec_start_index
            while window[window_index] - window[window_59_sec_start_index] > 59:
                print(window_59_sec_start_index, window_index)
                window_59_sec_start_index += 1
            for time in range(prev_start_index, window_59_sec_start_index):
                request_count = request_time_frequency.get(window[time], None)
                total_59_sec_request_count -= request_count

        if current_count is None:
            current_count = 1
        else:
            current_count += 1

        if current_count > 3 or total_10_sec_request_count > 20 or total_59_sec_request_count > 60:
            drop_count += 1
        request_time_frequency[requestTime[index]] = current_count

    return drop_count
