total = 0
count = 0
number = int(input("Число (0 — конец): "))
while number != 0:
    total += number
    count += 1
    number = int(input("Число (0 — конец): "))
print("Сумма:", total)
print("Количество:", count)
