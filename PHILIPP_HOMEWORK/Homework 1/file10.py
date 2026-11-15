attendance = int(input("Посещаемость, %: "))
labs = int(input("Сдано лабораторных: "))
debt = int(input("Долг по оплате, руб.: "))

attendance_ok = attendance >= 75
labs_ok = labs >= 8
no_debt = debt == 0
admitted = attendance_ok and labs_ok and no_debt

print("Посещаемость:", attendance_ok)
print("Лабораторные:", labs_ok)
print("Нет долга:", no_debt)
print("Допущен:", admitted)
