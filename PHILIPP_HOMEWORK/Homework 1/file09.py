price1 = int(input("Цена первого товара, руб.: "))
price2 = int(input("Цена второго товара, руб.: "))

coupon_works = (price1 > 1000) != (price2 > 1000)
print(coupon_works)
