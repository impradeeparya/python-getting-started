class Solution(object):

    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """

        output = []
        line_number = 0
        while line_number < len(source):

            line = source[line_number]

            single_comment_index = line.find("//")
            multi_line_comment_index = line.find("/*")

            output_line = None

            if single_comment_index != -1 or multi_line_comment_index != -1:
                if single_comment_index != -1 and multi_line_comment_index != -1:
                    if single_comment_index < multi_line_comment_index:
                        output_line = line[0:single_comment_index]
                    else:
                        start_line = line[0:multi_line_comment_index]
                        end_index = line.find("*/", multi_line_comment_index + 2)
                        print("while", line, start_line)
                        while end_index == -1 and line_number < len(source):
                            line_number = line_number + 1
                            line = source[line_number]
                            end_index = line.find("*/")
                            print("while", line, end_index, line_number)

                        if end_index != -1:
                            single_comment_index = line.find("//", end_index + 2)
                            max_length = single_comment_index if single_comment_index != -1 else len(line)
                            end_line = line[end_index + 2: max_length]
                            output_line = start_line + end_line
                elif multi_line_comment_index >= 0:
                    start_line = line[0:multi_line_comment_index]
                    end_index = line.find("*/", multi_line_comment_index + 2)
                    print("while", line, start_line)
                    while end_index == -1 and line_number < len(source):
                        line_number = line_number + 1
                        line = source[line_number]
                        end_index = line.find("*/")
                        print("while", line, end_index, line_number)

                    if end_index != -1:
                        single_comment_index = line.find("//", end_index + 2)
                        max_length = single_comment_index if single_comment_index != -1 else len(line)
                        end_line = line[end_index + 2: max_length]
                        output_line = start_line + end_line
                else:
                    output_line = line[0:single_comment_index]

            else:
                output_line = line
            if output_line:
                output.append(output_line)

            line_number = line_number + 1

        return output


print(Solution().removeComments(
    ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test",
     "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]))
print(Solution().removeComments(["a//*b//*c", "blank", "d/*/e*//f"]))
