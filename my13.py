A = [int(i) for i in input('Введите массив: ').split()]
print(A)
zn = max(A)
count = 0
for j in range(len(A)):
    if A[j] == max(A):
        count += 1
print('Максимальное значение: ', max(A))
print('Количество элементов', count)
1111
1414
