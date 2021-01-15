class Solution(object):
    def isValid(self, s):
        is_valid = True
        stack = []
        start_parenthesis = '{[('
        parentheses_map = {']': '[', '}': '{', ')': '('}
        for parenthesis in s:
            if parenthesis in start_parenthesis:
                stack.append(parenthesis)
            elif not stack:
                is_valid = False
                break
            else:
                top_element = stack.pop()
                if parentheses_map[parenthesis] != top_element:
                    is_valid = False
                    break
        return is_valid and not stack


print(Solution().isValid("}"))
