on_time = input("Сдана в срок (да/нет): ")
score = int(input("Баллы: "))

if score < 0 or score > 10:
    print("Ошибка ввода")
elif on_time == "да":
    if score >= 9:
        print("Оценка: 5")
    elif score >= 7:
        print("Оценка: 4")
    elif score >= 5:
        print("Оценка: 3")
    else:
        print("Работа не зачтена")
else:
    if score >= 5:
        print("Оценка: 3")
    else:
        print("Работа не зачтена")
