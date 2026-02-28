import random

# 1. Створіть двовимірний масив 3x3 з випадкових цілих чисел від 1 до 100
matrix = [[random.randint(1, 100) for _ in range(3)] for _ in range(3)]

print("Масив 3х3:")
for row in matrix:
    print(row)

# 2. Обчисліть суму всіх елементів масиву.
total_sum = sum(sum(row)for row in matrix)
print("\nСума всіх елементів:", total_sum)

# 3. Знайдіть максимальне та мінімальне значення в масиві, а також їхні індекси.
max_val = matrix[0][0]
min_val = matrix[0][0]
max_index = 0
min_index = 0
for i in range(3):
    for j in range(3):
        if matrix[i][j] > max_val:
            max_val = matrix[i][j]
            max_index = (i, j)
        if matrix[i][j] < min_val:
            min_val = matrix[i][j]
            min_index = (i, j)

print("Максимальне значення:", max_val, "Індекс:", max_index)
print("Максимальне значення:", min_val, "Індекс:", min_index)

# 4. Відсортуйте масив по кожному рядку.
sorted_matrix = [sorted(row) for row in matrix]

print("Відсортований масив:")
for row in sorted_matrix:
    print(row)