n = int(input("Число показаний: "))
first_temp = int(input("Показание, °C: "))
min_temp = first_temp
total = first_temp

for _ in range(n - 1):
    temp = int(input("Показание, °C: "))
    total += temp
    if temp < min_temp:
        min_temp = temp

print(f"Минимум: {min_temp}")
print(f"Среднее: {total / n:.2f}")
