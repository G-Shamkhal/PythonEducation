print((lambda nums: len(nums) != len(set(nums)))(list(map(int, input("Введите последовательность целых чисел через пробел: ").split()))))
