paid = input("Заказ оплачен (да/нет): ")
in_stock = input("Товар есть (да/нет): ")
has_address = input("Адрес указан (да/нет): ")

can_ship = paid == "да" and in_stock == "да" and has_address == "да"
need_call = paid == "да" and has_address == "нет"

print("Можно отправлять:", can_ship)
print("Позвонить покупателю:", need_call)
