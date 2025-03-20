inp = input("Введите несколько слов разделенных пробелом: ")

word = ''

for i, char in enumerate(inp):
    if char == ' ' or char == '\0':
        word += inp[i-1]
word += inp[-1]

print(word)
