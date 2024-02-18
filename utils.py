def power_five(num):
    degree = 0
    while 5 ** degree <= num:
        if 5 ** degree == num:
            return True
        degree += 1

    return False

number = int(input("Введіть число: "))
result = power_five(number)

if result:
    print(f"{number} є степенем п'ятірки.")
else:
    print(f"{number} не є степенем п'ятірки.")