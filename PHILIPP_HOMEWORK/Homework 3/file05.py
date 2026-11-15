for _ in range(3):
    pin = input("PIN-код: ")
    if pin == "4821":
        print("Доступ разрешён")
        break
else:
    print("Карта заблокирована")
