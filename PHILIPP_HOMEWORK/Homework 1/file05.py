exam1 = int(input("Балл за первый экзамен: "))
exam2 = int(input("Балл за второй экзамен: "))
exam3 = int(input("Балл за третий экзамен: "))

passed_count = (exam1 >= 40) + (exam2 >= 40) + (exam3 >= 40)
all_passed = passed_count == 3

print("Сдано экзаменов:", passed_count)
print("Сессия закрыта:", all_passed)
