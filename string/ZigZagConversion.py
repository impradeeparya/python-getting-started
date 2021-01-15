from collections import defaultdict

class Solution(object):
    def convert(self, s, numRows):
        output_string = ""
        column_diff = numRows - 1 + numRows - 2 - 1
        for row in range(numRows):
            column = row
            is_first_column = True
            while column < len(s):
                output_string = output_string + s[column]
                if (row == 0) or (row == numRows - 1):
                    column = column + (numRows - 1) + ((numRows - 2) if numRows > 1 else 0) + 1
                else:
                    column = column + column_diff if is_first_column else column + (row * 2)
                    is_first_column = not is_first_column
            column_diff = column_diff if row == 0 or row == numRows - 1 else column_diff - 2

        return output_string

    def convert1(self, s: str, numRows: int) -> str:
        if numRows == 1 or not s or len(s) < 2:
            return s
        dict_result = defaultdict(list)
        num_zig_zag = numRows * 2 - 2
        print(num_zig_zag)
        for index, value in enumerate(s):
            print(index, index % num_zig_zag, numRows - (2 + index % num_zig_zag - numRows))
            if index % num_zig_zag < numRows:
                dict_result[index % num_zig_zag].append(value)
            elif index % num_zig_zag >= numRows:
                dict_result[numRows - (2 + index % num_zig_zag - numRows)].append(value)
            print(dict_result)
        str_result = ''
        for key in dict_result:
            str_result = str_result + ''.join(dict_result[key])
        return str_result


output = Solution().convert1("PAYPALISHIRING", 4)
print(output)
