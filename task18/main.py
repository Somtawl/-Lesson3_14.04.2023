from random import randint

array = []
array_size = int(input("Укажите количество элементов в массиве "))
array_min = int(input("Укажите минимальное значения для чисел массива "))
array_max = int(input("Укажите максимальное значение для чисел в массиве "))
num = int(input("Какое число ищем ? "))
i = 0
count = 0
dif = array_max
result = array_max + 1

while i < array_size:
    array.append(randint(array_min,array_max))
    i = i + 1

for i in array:
    if abs(num - i) < dif:
        dif = abs(num - i)
        result = i

print("Массив",array)
print("Ближайшее число",result)