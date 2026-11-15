start = int(input("Начало интервала, ч: "))
end = int(input("Конец интервала, ч: "))
arrival = int(input("Курьер приехал, ч: "))

if arrival < start:
    print("Раньше интервала")
elif arrival <= end:
    print("Вовремя")
else:
    print(f"Опоздание на {arrival - end} ч")
