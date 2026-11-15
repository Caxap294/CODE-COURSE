months = int(input("Отработано месяцев: "))
requested_days = int(input("Дней отпуска: "))

if months < 6:
    print("Отпуск пока недоступен")
else:
    available_days = (months * 28) // 12
    print(f"Доступно дней: {available_days}")
    if requested_days <= available_days:
        print("Отпуск согласован")
    else:
        print(f"Не хватает дней: {requested_days - available_days}")
