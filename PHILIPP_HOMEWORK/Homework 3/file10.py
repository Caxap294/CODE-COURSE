n = int(input("Число покупок: "))
total_price = 0
for _ in range(n):
    price = int(input("Цена покупки, руб.: "))
    total_price += price
print(f"Итого: {total_price} руб.")
