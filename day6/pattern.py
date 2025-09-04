n = int(input("Enter a number: "))
rows = 2 * n - 1
for i in range(rows):
    for j in range(rows):
        min_dist = min(i, j, rows - 1 - i, rows - 1 - j)
        value_to_print = n - min_dist
        print(value_to_print, end=" ")
    print()