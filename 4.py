num = int(input("Введите число :"))
fl = 1
max = 0
num_new = num
while (num / fl) > 1:
    fl = fl * 10
while fl > 1:
    fl = fl / 10
    num_sm = (int(num_new / fl))
    num_new = num_new - (fl * num_sm)
    if num_sm > max:
        max = num_sm
print(f" Максимальное число : {max}")

