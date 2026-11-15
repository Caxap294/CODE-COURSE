height = int(input("Рост, см: "))
age = int(input("Возраст: "))
with_adult = input("Со взрослым (да/нет): ")

allowed = height >= 120 and (age >= 10 or with_adult == "да")
print("Можно на аттракцион:", allowed)
