inp = input("Введите 3 числа разеляя пробелом: ")

nums = []

for char in inp:
    if char.isdigit():
        nums.append(int(char))

for i in range(len(nums)-1):
    for j in range(len(nums)-1-i):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]

print(nums[1])
