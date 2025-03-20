import math
a = int(input("Введите длину стороны квадрата: "))
print(f"Площадь:\t{a ** 2}\n"
      f"Периметр:\t{4 * a}\n"
      f"Диагональ:\t{(a * math.sqrt(2)):.2f}")
