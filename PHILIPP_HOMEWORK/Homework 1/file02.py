age = int(input("Возраст: "))

is_discounted = age < 18 or age >= 65
is_full = not is_discounted

print("Льготный билет:", is_discounted)
print("Полный билет:", is_full)
