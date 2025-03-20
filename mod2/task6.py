import re

s = input("Введите строку состоящую из 0 и 1: ")
count_0 = (re.findall(r"[0]+", s) or [''])[0]
count_1 = (re.findall(r"[1]+", s) or [''])[0]
print("yes" if len(count_0) == len(count_1) else "no")
