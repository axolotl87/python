# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

list = [1, 7, 9, 25, -111, 16]
list2 = []
for i in list:
    sqr = i ** 0.5
    if i>=0 and int(sqr) == float(sqr):
        list2.append(int(sqr))
print(list2)
