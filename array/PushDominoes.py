class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes_length = len(dominoes)
        output = ['.'] * dominoes_length

        left_dominoes = [-1] * dominoes_length
        right_dominoes = [-1] * dominoes_length

        value = -1
        for index, element in enumerate(dominoes):
            if element != '.':
                output[index] = element
                value = index

            if element == '.' and value != -1 and dominoes[value] != 'R':
                value = -1
            left_dominoes[index] = value

        value = -1
        for index in range(dominoes_length - 1, -1, -1):
            element = dominoes[index]
            if element != '.':
                value = index
            if element == '.' and value != -1 and dominoes[value] != 'L':
                value = -1
            right_dominoes[index] = value

        # print(left_dominoes, right_dominoes)

        for index in range(dominoes_length):
            left_value = left_dominoes[index]
            right_value = right_dominoes[index]
            if left_value == right_value:
                output[index] = '.' if left_value == -1 else dominoes[left_value]
            elif left_value == -1 or right_value == -1:
                output[index] = dominoes[left_value] if left_value != -1 else dominoes[right_value]
            else:

                left = dominoes[left_value]
                right = dominoes[right_value]
                while left_value < right_value:
                    output[left_value] = left
                    output[right_value] = right
                    left_value += 1
                    right_value -= 1

                if left_value == right_value:
                    output[left_value] = '.'

        return "".join(output)


print('output "RR.L" ', Solution().pushDominoes(dominoes="RR.L"))
print('output "LL.RR.LLRRLL.." ', Solution().pushDominoes(dominoes=".L.R...LR..L.."))
