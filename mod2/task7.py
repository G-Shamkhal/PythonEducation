input_data = input("Введите строку и символ разделенные запятой: ")
i = input_data[-1]
s = input_data[:-2]
count = 0
for char in s:
    if char == i:
        count += 1
    else:
        break
print(count)
