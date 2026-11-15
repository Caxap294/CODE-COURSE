day = int(input("День недели (1–7): "))
hour = int(input("Час (0–23): "))

if (1 <= day <= 5 and 9 <= hour < 18) or (day == 6 and 10 <= hour < 15):
    print("Оператор на связи")
else:
    print("Оставьте заявку, ответим в рабочее время")
