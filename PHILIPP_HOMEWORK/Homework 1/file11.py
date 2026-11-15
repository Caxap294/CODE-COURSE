cash1 = input("Касса 1 открыта (да/нет): ")
cash2 = input("Касса 2 открыта (да/нет): ")
cash3 = input("Касса 3 открыта (да/нет): ")

only_one_open = (cash1 == "да") + (cash2 == "да") + (cash3 == "да") == 1
print(only_one_open)
