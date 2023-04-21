from random import randint

array = []
array_size = int(input("Укажите количество элементов в массиве "))
array_min = int(input("Укажите минимальное значения для чисел массива "))
array_max = int(input("Укажите максимальное значение для чисел в массиве "))
num = int(input("Какое число ищем ? "))
i = 0
count = 0

while i < array_size:
    array.append(randint(array_min,array_max + 1))
    i = i + 1

for i in array:
    if i == num:
        count = count + 1

print("Массив", array)
print("Число", num,"Встречается в массиве", count,"раз/раза")