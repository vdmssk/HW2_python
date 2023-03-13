prev = int(input("Введите число: "))
count = 1
max_count = 0

while True:
    num = int(input("Введите число: "))
    if num == 0:
        break
    if num == prev:
        count = 1
    elif (num > prev and count > 0) or (num < prev and count < 0):
        count += 1
    else:
        count = 2
    prev = num
    max_count = max(max_count, count)

print("Наибольшая длина:", max_count)
