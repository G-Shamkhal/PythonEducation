import sys


def convert(n, num_sys):
    digits = "0123456789ABCDEF"
    result = ""
    while n > 0:
        tmp = n % num_sys
        result = digits[tmp] + result
        n //= num_sys
    return result or "0"


num = int(input("Введите натуральное число: "))

if num <= 0:
    print("Неверный ввод")
    sys.exit()

binary = convert(num, 2)
octal = convert(num, 8)
hex_ = convert(num, 16)

print(f"Двоичное представление: {binary}")
print(f"Восьмеричное представление: {octal}")
print(f"Шестнадцатеричное представление: {hex_}")
