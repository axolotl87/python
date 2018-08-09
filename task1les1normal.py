number=int(input('введите число: '))
while number<0 or number>10:
    print("введите число еще раз")
    number = int(input('введите число: '))
res=number**2
print(res)