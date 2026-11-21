
def row_sums(matrix):
    """Возвращает список сумм строк матрицы."""
    return [sum(row) for row in matrix]


def column_sums(matrix):
    """Возвращает список сумм столбцов прямоугольной матрицы."""
    if not matrix:
        return []

    columns = len(matrix[0])
    return [sum(row[column] for row in matrix) for column in range(columns)]


def diagonal_pattern(size):
    """Создаёт квадратную таблицу size × size по заданному правилу."""
    table = []

    for row in range(size):
        current_row = []
        for column in range(size):
            if row == column:
                current_row.append(0)
            elif row < column:
                current_row.append(1)
            else:
                current_row.append(2)
        table.append(current_row)
    return table

def transform(matrix):
    """Вариант 10: элементы с модулем больше 4 заменить нулями."""
    result = []
    for row in matrix:
        new_row = []
        for value in row:
            if abs(value) > 4:
                new_row.append(0)
            else:
                new_row.append(value)
        result.append(new_row)
    return result