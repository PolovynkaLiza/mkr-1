# Введення масиву NxN
n = int(input("Введіть розмірність масиву (NxN): "))
matrix = []

print("Введіть рядки масиву:")
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Сортування масиву за середнім значенням рядків
sorted_matrix = sorted(matrix, key=lambda row: sum(row) / len(row))

# Виведення відсортованого масиву
print("Відсортований масив за зростанням середнього значення рядків:")
for row in sorted_matrix:
    print(row)