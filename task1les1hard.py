name = input('введите имя: ')
surname = input('введите фамилию: ')
age = int(input('введите возраст: '))
weight = int(input('введите вес: '))
if age < 30 and 50 <= weight <= 120:
    print(name, surname, age, weight, ' - вы в хорошем состянии')
elif age >= 30 and 50 > weight > 120:
    print(name, surname, age, weight, ' - вам следует вести здоровый образ жизни')
    if age > 40:
        print(name, surname, age, weight, ' - вам следует обратиться к врачу')
else:
    print (' - вам следует обратить внимание на свой вес')