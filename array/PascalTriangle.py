class PascalTriangle(object):

    def binomial_coefficient(self, line, index):
        # C(n r) = n!/((n-r)! * r!)
        n_factorial = 1
        for number in range(1, line + 1):
            n_factorial = n_factorial * number
        n_r_factorial = 1
        for number in range(1, (line - index) + 1):
            n_r_factorial = n_r_factorial * number
        r_factorial = 1
        for number in range(1, index + 1):
            r_factorial = r_factorial * number

        return n_factorial / (n_r_factorial * r_factorial)

    def print_triangle(self, lines):
        for row in range(lines):
            for column in range(row + 1):
                print(int(self.binomial_coefficient(row, column)), end=' ')
            print()


PascalTriangle().print_triangle(5)
