def get_matrix (n, m, value):# объявляем функцию
    matrix = [] # создаем пустой список
    for i in range(n): # организуем внешний цикл для количества строк
        matrix.append([]) # добавляем список значениями
        for j in range(m): # организуем внутренний цикл для количества столбцов
            matrix[i].append(value) # добавляем в список значения
    print(matrix)
get_matrix(2, 2, 10) # вызов функции get_matrix
get_matrix(3, 5, 42) # вызов функции get_matrix
get_matrix(4, 2, 13) # вызов функции get_matrix






