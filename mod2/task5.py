import re
domain = input("Введите домен в формате www.domain.com: ")
pattern = r'^([a-zA-Z0-9-]+)\.([a-zA-Z0-9-]+)\.([a-zA-Z0-9-]+)$'
match = re.match(pattern, domain)
if match:
    print(f"{match.group(3)}\n{match.group(2)}\n{match.group(1)}")
else:
    print("Неверный формат домена")
