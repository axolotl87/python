# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruits1 = ['apple', 'banana', 'watermelon', 'kiwi']
fruits2 = ['pineapple', 'orange', 'mango', 'jackfruit','apple','kiwi']
fruits_cons = [i for i in set(fruits1 + fruits2)]
print(fruits_cons)
