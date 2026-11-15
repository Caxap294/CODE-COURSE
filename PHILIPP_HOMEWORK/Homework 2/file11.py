has_oms = input("Полис ОМС есть (да/нет): ")
age = int(input("Возраст: "))

if has_oms == "да":
    if age < 18:
        print("Запись к педиатру")
    else:
        print("Запись к терапевту")
else:
    print("Доступен платный приём")
