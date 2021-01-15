class ChampagneTower(object):
    def glass_quantity(self, poured, query_row, query_glass):
        query_row += 1
        query_glass += 1
        glasses = [0] * int((query_row * (query_row + 1)) / 2)
        index = 0
        glasses[index] = poured
        for row in range(1, query_row):
            for column in range(1, row + 1):
                glass_quantity = glasses[index]

                glasses[index] = 1.0 if glass_quantity >= 1.0 else glass_quantity
                glass_quantity = glass_quantity - 1 if glass_quantity >= 1.0 else 0.0
                glasses[row + index] += glass_quantity / 2
                glasses[row + index + 1] += glass_quantity / 2
                index += 1
        return glasses[int((query_row * (query_row - 1) / 2) + query_glass - 1)]


print(ChampagneTower().glass_quantity(2, 1, 1))
