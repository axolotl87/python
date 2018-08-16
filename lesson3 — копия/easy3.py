# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов





def str_lenght(*args):
    for arg in args:
        #result = max(args, key = len) - пробовал и так и так - не идет никак((
        lenght = len(arg)
    result = max(lenght)
    return result
string = list(input('input args: '))
result1 = str_lenght(*string)
print(result1)
