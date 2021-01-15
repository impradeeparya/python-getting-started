def mark_cluster(n, m, park_area):
    value = park_area[n][m]
    if value == 1:
        park_area[n][m] = 0
        if n < len(park_area) - 1:
            mark_cluster(n + 1, m, park_area)
        if n > 0:
            mark_cluster(n - 1, m, park_area)
        if m < len(park_area[0]) - 1:
            mark_cluster(n, m + 1, park_area)
        if m > 0:
            mark_cluster(n, m - 1, park_area)


def find_cluster(n, m, park_area):
    count = 0
    for row in range(n):
        for column in range(m):
            value = park_area[row][column]
            if value == 1:
                count += 1
                mark_cluster(row, column, park_area)

    return count


def find_treasure():
    park_area = [[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 1, 1], [1, 1, 1, 0]]
    n = len(park_area)
    m = len(park_area[0])

    for row in range(n):
        for column in range(m):
            print(park_area[row][column], end=" ")
        print()

    number_of_treasures = find_cluster(n, m, park_area)

    print('number of treasures : ', number_of_treasures)


find_treasure()
