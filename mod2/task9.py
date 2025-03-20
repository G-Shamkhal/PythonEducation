inp = input("Введите номер телефона: ")
result = ""

for char in inp:
    if char.isdigit() or char == '+':
        result += char

print(result)
