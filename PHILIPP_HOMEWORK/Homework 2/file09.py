a = int(input("Сторона a: "))
b = int(input("Сторона b: "))
c = int(input("Сторона c: "))

if a >= b + c or b >= a + c or c >= a + b:
    print("Треугольник не существует")
elif a == b == c:
    print("Равносторонний")
elif a == b or b == c or a == c:
    print("Равнобедренный")
else:
    print("Разносторонний")
