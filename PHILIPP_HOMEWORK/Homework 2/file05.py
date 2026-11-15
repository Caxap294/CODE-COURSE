charge = int(input("Заряд, %: "))

if charge <= 15:
    print("Критический заряд")
elif charge <= 50:
    print("Низкий заряд")
elif charge <= 99:
    print("Нормальный заряд")
else:
    print("Батарея заряжена")
