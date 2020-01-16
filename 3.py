num = int(input("Введите число :"))
fl = 1
while True:
    if (num / fl) > 1:
        fl = fl * 10
    else:
        num2 = (num * fl) + num
        num3 = (num2 * fl) + num
        break
print(f" {num} + {num2} + {num3} = {num + num2 + num3}")
