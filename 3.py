sum = 0
count = 0

while True:
    num = int(input("Введите число: "))
    if num == 0:
        break
    sum += num
    count += 1

if count > 0:
    avr = sum / count
    print("Среднее арифмет.: ", avr)
else:
    print("Нет чисел, чтобы рассчитывать среднее арифмет.")