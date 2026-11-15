n = int(input("Число n: "))
total = 0
for number in range(1, n + 1):
    total += number * number
print("Сумма квадратов:", total)
