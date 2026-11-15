secret = 37
for attempt in range(1, 6):
    guess = int(input("Ваша догадка: "))
    if guess < secret:
        print("Больше")
    elif guess > secret:
        print("Меньше")
    else:
        print(f"Угадано с попытки {attempt}")
        break
else:
    print("Попытки закончились")
