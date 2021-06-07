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

    def generate(self, numRows):
        triangle = []
        for row in range(numRows):
            row_elements = []
            for column in range(row + 1):
                row_elements.append(int(self.binomial_coefficient(row, column)))
            triangle.append(row_elements)
        return triangle


print(PascalTriangle().generate(5))
