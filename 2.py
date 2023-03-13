n = int(input("Введите количество чисел: "))
m = False

for i in range(n):
    num = int(input("Введите число: "))
    if num == 0:
        m = True

if m:
    print("YES")
else:
    print("NO")