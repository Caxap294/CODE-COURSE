total_steps = 0
steps = int(input("Шаги за день (0 — конец): "))
while steps != 0:
    total_steps += steps
    steps = int(input("Шаги за день (0 — конец): "))
print(f"Всего шагов: {total_steps}")
