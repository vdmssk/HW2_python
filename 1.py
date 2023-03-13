a = int(input("Введите число: "))
b = 2

while b <= a:
    if a % b == 0:
        print("Наименьший делитель числа", a, "отличный от 1: ", b)
        break
    b += 1