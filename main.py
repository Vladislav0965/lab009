from table import row_sums, column_sums, diagonal_pattern
def read_matrix():
    rows = int(input("Количество строк: "))
    columns = int(input("Количество столбцов: "))
    matrix = []
    for _ in range(rows):
        row = [int(part) for part in input("Строка таблицы: ").split()]
        while len(row) != columns:
            print(f"Нужно ровно {columns} чисел")
            row = [int(part) for part in input("Повторите строку: ").split()]
        matrix.append(row)
    return matrix
def main():
    matrix = read_matrix()
    print("Суммы строк:", row_sums(matrix))
    print("Суммы столбцов:", column_sums(matrix))
    size = 0
    while size < 1:
        size = int(input("Положительный размер узора: "))
    print("Диагональный узор:")
    for line in diagonal_pattern(size):
        print(*line)
if __name__ == "__main__":
    main()