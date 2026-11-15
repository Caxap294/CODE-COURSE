n = int(input("Натуральное число: "))
divisors_sum = 0
for i in range(1, n):
    if n % i == 0:
        divisors_sum += i

if n > 1 and divisors_sum == n:
    print("Совершенное")
else:
    print("Не совершенное")
