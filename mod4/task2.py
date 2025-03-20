def pow(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return pow(a * a, n // 2)
    else:
        return a * pow(a, n - 1)


a, n = map(int, input("Введите два целых чисел через пробел: ").split())
print(pow(a, n))
