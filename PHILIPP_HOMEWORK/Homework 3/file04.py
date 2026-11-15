order = int(input("Номер заказа: "))
digits_sum = 0
while order > 0:
    digits_sum += order % 10
    order //= 10
print(f"Сумма цифр: {digits_sum}")
