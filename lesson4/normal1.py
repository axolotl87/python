# Задача - 1
# Запросите у пользователя имя, фамилию, email. Теперь необходимо совершить проверки, имя и фамилия должны иметь заглавные первые буквы.
# email - не должен иметь заглавных букв и должен быть в формате: текст в нижнем регистре, допускается нижнее подчеркивание и цифры, потом @,
#  потом текст, допускаются цифры, точка, ru или org или com.
# Например:
# Пупкин василий - неверно указано имя, te$T@test.net - неверно указан email (спецсимвол, заглавная буква, .net), te_4_st@test.com - верно указан.

import re


data = input('Введите Имя, Фамилию, email: ')
data = data.split( )
ns = str(data[0] +' ' + data[1])
email = str(data[2])
#print(ns, email)
pattern1 = '^([А-Яа-я]+) ([А-Яа-я]+)'
pattern2 = '([a-z_0-9]+@[a-z0-9]+\.(ru|com|org))'
result1 = re.match(pattern1,ns)
if result1:
    print(ns)
else:
    print(ns,' - неверно указано имя')
result2 = re.search(pattern2,email)
if result2:
    print(email, ' - верно указана почта')
else:
    print('неверно указан email')
